import os
def w(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
rp = 'C:/Users/Asus/OneDrive/Desktop/khatta/garg-store/src/main/java/com/example/gargstore/repository/'

w(rp+'FinancialSummaryRepository.java', '''package com.example.gargstore.repository;
import com.example.gargstore.model.FinancialSummary; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.jdbc.core.JdbcTemplate; import org.springframework.jdbc.core.RowMapper; import org.springframework.stereotype.Repository; import java.util.List;
@Repository
public class FinancialSummaryRepository {
    @Autowired private JdbcTemplate jdbc;
    private RowMapper<FinancialSummary> mapper = (rs, rowNum) -> {
        FinancialSummary f = new FinancialSummary(); f.setPeriodId(rs.getString("Period_Id")); f.setPeriod(rs.getString("Period")); f.setTotalAssets(rs.getDouble("Total_Assets")); f.setTotalLiabilities(rs.getDouble("Total_Liabilities")); f.setOperatingCost(rs.getDouble("Operating_Cost")); f.setGrossProfit(rs.getDouble("Gross_Profit")); f.setNetProfit(rs.getDouble("Net_Profit")); f.setTax(rs.getDouble("Tax")); return f;
    };
    public List<FinancialSummary> findAll() { return jdbc.query("SELECT * FROM Financial_Summary", mapper); }
    public FinancialSummary findById(String id) { return jdbc.queryForObject("SELECT * FROM Financial_Summary WHERE Period_Id=?", mapper, id); }
}''')

w(rp+'EmployeeRepository.java', '''package com.example.gargstore.repository;
import com.example.gargstore.model.Employee; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.jdbc.core.JdbcTemplate; import org.springframework.jdbc.core.RowMapper; import org.springframework.stereotype.Repository; import java.util.List;
@Repository
public class EmployeeRepository {
    @Autowired private JdbcTemplate jdbc;
    private RowMapper<Employee> mapper = (rs, rowNum) -> {
        Employee e = new Employee(); e.setEmployeeCode(rs.getString("Employee_Code")); e.setName(rs.getString("Name")); e.setDesignation(rs.getString("Designation")); e.setPhoneNo(rs.getString("Phone_No")); e.setDateOfJoining(rs.getDate("Date_of_Joining")); e.setSalary(rs.getDouble("Salary")); e.setPeriodId(rs.getString("Period_Id")); return e;
    };
    public List<Employee> findAll() { return jdbc.query("SELECT * FROM Employee", mapper); }
    public Employee findById(String id) { return jdbc.queryForObject("SELECT * FROM Employee WHERE Employee_Code=?", mapper, id); }
    public int count() { return jdbc.queryForObject("SELECT COUNT(*) FROM Employee", Integer.class); }
}''')

w(rp+'SaleBillRepository.java', '''package com.example.gargstore.repository;
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
}''')

w(rp+'PurchaseBillRepository.java', '''package com.example.gargstore.repository;
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
}''')

w(rp+'PaymentReceivedRepository.java', '''package com.example.gargstore.repository;
import com.example.gargstore.model.PaymentReceived; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.jdbc.core.JdbcTemplate; import org.springframework.jdbc.core.RowMapper; import org.springframework.stereotype.Repository; import java.util.List;
@Repository
public class PaymentReceivedRepository {
    @Autowired private JdbcTemplate jdbc;
    private RowMapper<PaymentReceived> mapper = (rs, rowNum) -> {
        PaymentReceived p = new PaymentReceived(); p.setReceiptNo(rs.getString("Receipt_No")); p.setClientCode(rs.getString("Client_Code")); p.setDateReceived(rs.getDate("Date_Received")); p.setAmountReceived(rs.getDouble("Amount_Received")); p.setPaymentMode(rs.getString("Payment_Mode")); return p;
    };
    public List<PaymentReceived> findAll() { return jdbc.query("SELECT * FROM Payment_Received", mapper); }
    public int save(PaymentReceived p) { return jdbc.update("INSERT INTO Payment_Received (Receipt_No, Client_Code, Date_Received, Amount_Received, Payment_Mode) VALUES (?,?,?,?,?)", p.getReceiptNo(), p.getClientCode(), p.getDateReceived(), p.getAmountReceived(), p.getPaymentMode()); }
}''')
