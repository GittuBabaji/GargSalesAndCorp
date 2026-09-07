package com.example.gargstore.repository;
import com.example.gargstore.model.PurchaseBill; import com.example.gargstore.model.PurchaseBillItem; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.jdbc.core.JdbcTemplate; import org.springframework.jdbc.core.RowMapper; import org.springframework.stereotype.Repository; import java.util.List;
@Repository
public class PurchaseBillRepository {
    @Autowired private JdbcTemplate jdbc;
    private RowMapper<PurchaseBill> mapper = (rs, rowNum) -> {
        PurchaseBill p = new PurchaseBill(); p.setPurchaseBillNo(rs.getString("Purchase_Bill_No")); p.setBillDate(rs.getDate("Bill_Date")); p.setSupplierCode(rs.getString("Supplier_Code")); p.setTotalAmount(rs.getDouble("Total_Amount")); p.setAmountPaid(rs.getDouble("Amount_Paid")); p.setBalanceDue(rs.getDouble("Balance_Due")); p.setPeriodId(rs.getString("Period_Id")); return p;
    };
    private RowMapper<PurchaseBillItem> itemMapper = (rs, rowNum) -> {
        PurchaseBillItem p = new PurchaseBillItem(); p.setPurchaseBillNo(rs.getString("Purchase_Bill_No")); p.setItemCode(rs.getString("Item_Code")); p.setQuantity(rs.getInt("Quantity")); p.setRate(rs.getDouble("Rate")); p.setAmount(rs.getDouble("Amount")); return p;
    };
    public List<PurchaseBill> findAll() { return jdbc.query("SELECT * FROM Purchase_Bill", mapper); }
    public PurchaseBill findById(String id) { return jdbc.queryForObject("SELECT * FROM Purchase_Bill WHERE Purchase_Bill_No=?", mapper, id); }
    public List<PurchaseBillItem> findItems(String billNo) { return jdbc.query("SELECT * FROM Purchase_Bill_Item WHERE Purchase_Bill_No=?", itemMapper, billNo); }
    public int saveBill(PurchaseBill p) { return jdbc.update("INSERT INTO Purchase_Bill (Purchase_Bill_No, Bill_Date, Supplier_Code, Total_Amount, Amount_Paid, Balance_Due, Period_Id) VALUES (?,?,?,?,?,?,?)", p.getPurchaseBillNo(), p.getBillDate(), p.getSupplierCode(), p.getTotalAmount(), p.getAmountPaid(), p.getBalanceDue(), p.getPeriodId()); }
    public int saveItem(PurchaseBillItem i) { return jdbc.update("INSERT INTO Purchase_Bill_Item (Purchase_Bill_No, Item_Code, Quantity, Rate, Amount) VALUES (?,?,?,?,?)", i.getPurchaseBillNo(), i.getItemCode(), i.getQuantity(), i.getRate(), i.getAmount()); }
    public double getTotalPurchases() { Double v = jdbc.queryForObject("SELECT COALESCE(SUM(Total_Amount), 0) FROM Purchase_Bill", Double.class); return v==null?0:v; }
}
