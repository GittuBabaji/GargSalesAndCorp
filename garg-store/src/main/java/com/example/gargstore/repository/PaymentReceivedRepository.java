package com.example.gargstore.repository;
import com.example.gargstore.model.PaymentReceived; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.jdbc.core.JdbcTemplate; import org.springframework.jdbc.core.RowMapper; import org.springframework.stereotype.Repository; import java.util.List;
@Repository
public class PaymentReceivedRepository {
    @Autowired private JdbcTemplate jdbc;
    private RowMapper<PaymentReceived> mapper = (rs, rowNum) -> {
        PaymentReceived p = new PaymentReceived(); p.setReceiptNo(rs.getString("Receipt_No")); p.setClientCode(rs.getString("Client_Code")); p.setDateReceived(rs.getDate("Date_Received")); p.setAmountReceived(rs.getDouble("Amount_Received")); p.setPaymentMode(rs.getString("Payment_Mode")); return p;
    };
    public List<PaymentReceived> findAll() { return jdbc.query("SELECT * FROM Payment_Received", mapper); }
    public int save(PaymentReceived p) { return jdbc.update("INSERT INTO Payment_Received (Receipt_No, Client_Code, Date_Received, Amount_Received, Payment_Mode) VALUES (?,?,?,?,?)", p.getReceiptNo(), p.getClientCode(), p.getDateReceived(), p.getAmountReceived(), p.getPaymentMode()); }
}
