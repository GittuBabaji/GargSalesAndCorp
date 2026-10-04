package com.example.gargstore.repository;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;
import com.example.gargstore.model.Supplier;

@Repository
public class SupplierRepository {
    @Autowired
    private JdbcTemplate jdbc;

    private RowMapper<Supplier> mapper = (rs, rowNum) -> {
        Supplier s = new Supplier();
        s.setSupplierCode(rs.getString("Supplier_Code"));
        s.setName(rs.getString("Name"));
        s.setAddress(rs.getString("Address"));
        s.setLocality(rs.getString("Locality"));
        s.setPhoneNo(rs.getString("Phone_No"));
        s.setGstNo(rs.getString("GST_No"));
        return s;
    };

    private RowMapper<Supplier> summaryMapper = (rs, rowNum) -> {
        Supplier s = new Supplier();
        s.setSupplierCode(rs.getString("Supplier_Code"));
        s.setName(rs.getString("Name"));
        s.setAddress(rs.getString("Address"));
        s.setLocality(rs.getString("Locality"));
        s.setPhoneNo(rs.getString("Phone_No"));
        s.setGstNo(rs.getString("GST_No"));
        s.setTotalPurchases(rs.getDouble("total_purchases"));
        s.setTotalBills(rs.getInt("total_bills"));
        s.setTotalPaid(rs.getDouble("total_paid"));
        s.setTotalDue(rs.getDouble("total_due"));
        return s;
    };

    private static final String SUPPLIER_SUMMARY_SQL = 
        "SELECT s.*, " +
        "       COALESCE(pb.total_purchases, 0) AS total_purchases, " +
        "       COALESCE(pb.total_bills, 0) AS total_bills, " +
        "       COALESCE(pb.total_paid, 0) AS total_paid, " +
        "       COALESCE(pb.total_due, 0) AS total_due " +
        "FROM Supplier s " +
        "LEFT JOIN ( " +
        "    SELECT Supplier_Code, " +
        "           SUM(Total_Amount) AS total_purchases, " +
        "           COUNT(*) AS total_bills, " +
        "           SUM(Amount_Paid) AS total_paid, " +
        "           SUM(Balance_Due) AS total_due " +
        "    FROM Purchase_Bill " +
        "    GROUP BY Supplier_Code " +
        ") pb ON s.Supplier_Code = pb.Supplier_Code ";

    public List<Supplier> findAll() {
        return jdbc.query("SELECT * FROM Supplier ORDER BY Supplier_Code", mapper);
    }

    public List<Supplier> findPagedWithSummary(int page, int size) {
        int offset = Math.max(0, (page - 1) * size);
        String sql = SUPPLIER_SUMMARY_SQL + "ORDER BY s.Supplier_Code LIMIT ? OFFSET ?";
        return jdbc.query(sql, summaryMapper, size, offset);
    }

    public Supplier findById(String code) {
        return jdbc.queryForObject("SELECT * FROM Supplier WHERE Supplier_Code = ?", mapper, code);
    }

    public Supplier findByIdWithSummary(String code) {
        String sql = SUPPLIER_SUMMARY_SQL + "WHERE s.Supplier_Code = ?";
        return jdbc.queryForObject(sql, summaryMapper, code);
    }

    public int save(Supplier s) {
        return jdbc.update(
                "INSERT INTO Supplier (Supplier_Code, Name, Address, Locality, Phone_No, GST_No) VALUES (?,?,?,?,?,?)",
                s.getSupplierCode(), s.getName(), s.getAddress(), s.getLocality(), s.getPhoneNo(), s.getGstNo());
    }

    public int update(Supplier s) {
        return jdbc.update(
                "UPDATE Supplier SET Name=?, Address=?, Locality=?, Phone_No=?, GST_No=? WHERE Supplier_Code=?",
                s.getName(), s.getAddress(), s.getLocality(), s.getPhoneNo(), s.getGstNo(), s.getSupplierCode());
    }

    public int delete(String code) {
        return jdbc.update("DELETE FROM Supplier WHERE Supplier_Code=?", code);
    }

    public int count() {
        Integer cnt = jdbc.queryForObject("SELECT COUNT(*) FROM Supplier", Integer.class);
        return cnt == null ? 0 : cnt;
    }

    public double getTotalPurchases() {
        Double val = jdbc.queryForObject("SELECT COALESCE(SUM(Total_Amount), 0) FROM Purchase_Bill", Double.class);
        return val == null ? 0.0 : val;
    }

    public double getTotalPaid() {
        Double val = jdbc.queryForObject("SELECT COALESCE(SUM(Amount_Paid), 0) FROM Purchase_Bill", Double.class);
        return val == null ? 0.0 : val;
    }

    public double getTotalBalanceDue() {
        Double val = jdbc.queryForObject("SELECT COALESCE(SUM(Balance_Due), 0) FROM Purchase_Bill", Double.class);
        return val == null ? 0.0 : val;
    }
}
