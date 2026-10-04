package com.example.gargstore.repository;
import com.example.gargstore.model.SaleBill; import com.example.gargstore.model.SaleBillItem; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.jdbc.core.JdbcTemplate; import org.springframework.jdbc.core.RowMapper; import org.springframework.stereotype.Repository; import java.util.List;
@Repository
public class SaleBillRepository {
    @Autowired private JdbcTemplate jdbc;
    private RowMapper<SaleBill> mapper = (rs, rowNum) -> {
        SaleBill s = new SaleBill(); s.setBillNo(rs.getString("Bill_No")); s.setBillDate(rs.getDate("Bill_Date")); s.setClientCode(rs.getString("Client_Code")); s.setTotalAmount(rs.getDouble("Total_Amount")); s.setPaymentMode(rs.getString("Payment_Mode")); s.setBalanceDue(rs.getDouble("Balance_Due")); s.setPeriodId(rs.getString("Period_Id")); return s;
    };
    private RowMapper<SaleBillItem> itemMapper = (rs, rowNum) -> {
        SaleBillItem s = new SaleBillItem(); s.setBillNo(rs.getString("Bill_No")); s.setItemCode(rs.getString("Item_Code")); s.setQuantitySold(rs.getInt("Quantity_Sold")); s.setRateApplied(rs.getDouble("Rate_Applied")); s.setAmount(rs.getDouble("Amount")); return s;
    };
    public List<SaleBill> findAll() { return jdbc.query("SELECT * FROM Sale_Bill", mapper); }
    public SaleBill findById(String id) { return jdbc.queryForObject("SELECT * FROM Sale_Bill WHERE Bill_No=?", mapper, id); }
    public List<SaleBillItem> findItems(String billNo) { return jdbc.query("SELECT * FROM Sale_Bill_Item WHERE Bill_No=?", itemMapper, billNo); }
    public int saveBill(SaleBill s) { return jdbc.update("INSERT INTO Sale_Bill (Bill_No, Bill_Date, Client_Code, Total_Amount, Payment_Mode, Balance_Due, Period_Id) VALUES (?,?,?,?,?,?,?)", s.getBillNo(), s.getBillDate(), s.getClientCode(), s.getTotalAmount(), s.getPaymentMode(), s.getBalanceDue(), s.getPeriodId()); }
    public int saveItem(SaleBillItem i) { return jdbc.update("INSERT INTO Sale_Bill_Item (Bill_No, Item_Code, Quantity_Sold, Rate_Applied, Amount) VALUES (?,?,?,?,?)", i.getBillNo(), i.getItemCode(), i.getQuantitySold(), i.getRateApplied(), i.getAmount()); }
    public double getTotalSales() { Double v = jdbc.queryForObject("SELECT COALESCE(SUM(Total_Amount), 0) FROM Sale_Bill", Double.class); return v==null?0:v; }
}
