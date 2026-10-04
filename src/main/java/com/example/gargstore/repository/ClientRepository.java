package com.example.gargstore.repository;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;
import com.example.gargstore.model.Client;

@Repository
public class ClientRepository {
    @Autowired
    private JdbcTemplate jdbc;

    private RowMapper<Client> mapper = (rs, rowNum) -> {
        Client c = new Client();
        c.setClientCode(rs.getString("Client_Code"));
        c.setName(rs.getString("Name"));
        c.setAddress(rs.getString("Address"));
        c.setLocality(rs.getString("Locality"));
        c.setPhoneNo(rs.getString("Phone_No"));
        c.setGstNo(rs.getString("GST_No"));
        c.setDrBalance(rs.getDouble("DR_Balance"));
        c.setCrBalance(rs.getDouble("CR_Balance"));
        return c;
    };

    private RowMapper<Client> summaryMapper = (rs, rowNum) -> {
        Client c = new Client();
        c.setClientCode(rs.getString("Client_Code"));
        c.setName(rs.getString("Name"));
        c.setAddress(rs.getString("Address"));
        c.setLocality(rs.getString("Locality"));
        c.setPhoneNo(rs.getString("Phone_No"));
        c.setGstNo(rs.getString("GST_No"));
        c.setDrBalance(rs.getDouble("DR_Balance"));
        c.setCrBalance(rs.getDouble("CR_Balance"));
        c.setTotalSales(rs.getDouble("total_sales"));
        c.setTotalBills(rs.getInt("total_bills"));
        c.setTotalDue(rs.getDouble("total_due"));
        c.setTotalPaid(rs.getDouble("total_paid"));
        return c;
    };

    private static final String CLIENT_SUMMARY_SQL = 
        "SELECT c.*, " +
        "       COALESCE(sb.total_sales, 0) AS total_sales, " +
        "       COALESCE(sb.total_bills, 0) AS total_bills, " +
        "       COALESCE(sb.total_due, 0) AS total_due, " +
        "       COALESCE(pr.total_paid, 0) AS total_paid " +
        "FROM Client c " +
        "LEFT JOIN ( " +
        "    SELECT Client_Code, " +
        "           SUM(Total_Amount) AS total_sales, " +
        "           COUNT(*) AS total_bills, " +
        "           SUM(Balance_Due) AS total_due " +
        "    FROM Sale_Bill " +
        "    GROUP BY Client_Code " +
        ") sb ON c.Client_Code = sb.Client_Code " +
        "LEFT JOIN ( " +
        "    SELECT Client_Code, " +
        "           SUM(Amount_Received) AS total_paid " +
        "    FROM Payment_Received " +
        "    GROUP BY Client_Code " +
        ") pr ON c.Client_Code = pr.Client_Code ";

    public List<Client> findAll() {
        return jdbc.query("SELECT * FROM Client ORDER BY Client_Code", mapper);
    }

    public List<Client> findPagedWithSummary(int page, int size) {
        int offset = Math.max(0, (page - 1) * size);
        String sql = CLIENT_SUMMARY_SQL + "ORDER BY c.Client_Code LIMIT ? OFFSET ?";
        return jdbc.query(sql, summaryMapper, size, offset);
    }

    public Client findById(String code) {
        return jdbc.queryForObject("SELECT * FROM Client WHERE Client_Code = ?", mapper, code);
    }

    public Client findByIdWithSummary(String code) {
        String sql = CLIENT_SUMMARY_SQL + "WHERE c.Client_Code = ?";
        return jdbc.queryForObject(sql, summaryMapper, code);
    }

    public int save(Client c) {
        return jdbc.update(
                "INSERT INTO Client (Client_Code, Name, Address, Locality, Phone_No, GST_No, DR_Balance, CR_Balance) VALUES (?,?,?,?,?,?,?,?)",
                c.getClientCode(), c.getName(), c.getAddress(), c.getLocality(), c.getPhoneNo(), c.getGstNo(),
                c.getDrBalance(), c.getCrBalance());
    }

    public int update(Client c) {
        return jdbc.update(
                "UPDATE Client SET Name=?, Address=?, Locality=?, Phone_No=?, GST_No=?, DR_Balance=?, CR_Balance=? WHERE Client_Code=?",
                c.getName(), c.getAddress(), c.getLocality(), c.getPhoneNo(), c.getGstNo(), c.getDrBalance(),
                c.getCrBalance(), c.getClientCode());
    }

    public int delete(String code) {
        return jdbc.update("DELETE FROM Client WHERE Client_Code=?", code);
    }

    public int count() {
        Integer cnt = jdbc.queryForObject("SELECT COUNT(*) FROM Client", Integer.class);
        return cnt == null ? 0 : cnt;
    }

    public double getTotalSales() {
        Double val = jdbc.queryForObject("SELECT COALESCE(SUM(Total_Amount), 0) FROM Sale_Bill", Double.class);
        return val == null ? 0.0 : val;
    }

    public double getTotalPayments() {
        Double val = jdbc.queryForObject("SELECT COALESCE(SUM(Amount_Received), 0) FROM Payment_Received", Double.class);
        return val == null ? 0.0 : val;
    }

    public double getTotalBalanceDue() {
        Double val = jdbc.queryForObject("SELECT COALESCE(SUM(Balance_Due), 0) FROM Sale_Bill", Double.class);
        return val == null ? 0.0 : val;
    }

    public double getTotalDrBalance() {
        Double val = jdbc.queryForObject("SELECT COALESCE(SUM(DR_Balance), 0) FROM Client", Double.class);
        return val == null ? 0.0 : val;
    }

    public double getTotalCrBalance() {
        Double val = jdbc.queryForObject("SELECT COALESCE(SUM(CR_Balance), 0) FROM Client", Double.class);
        return val == null ? 0.0 : val;
    }
}
