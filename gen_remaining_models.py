import os
def w(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
md = 'C:/Users/Asus/OneDrive/Desktop/khatta/garg-store/src/main/java/com/example/gargstore/model/'

w(md+'FinancialSummary.java', '''package com.example.gargstore.model;
public class FinancialSummary {
    private String periodId; private String period; private double totalAssets; private double totalLiabilities; private double operatingCost; private double grossProfit; private double netProfit; private double tax;
    // getters setters
    public String getPeriodId(){return periodId;} public void setPeriodId(String v){periodId=v;}
    public String getPeriod(){return period;} public void setPeriod(String v){period=v;}
    public double getTotalAssets(){return totalAssets;} public void setTotalAssets(double v){totalAssets=v;}
    public double getTotalLiabilities(){return totalLiabilities;} public void setTotalLiabilities(double v){totalLiabilities=v;}
    public double getOperatingCost(){return operatingCost;} public void setOperatingCost(double v){operatingCost=v;}
    public double getGrossProfit(){return grossProfit;} public void setGrossProfit(double v){grossProfit=v;}
    public double getNetProfit(){return netProfit;} public void setNetProfit(double v){netProfit=v;}
    public double getTax(){return tax;} public void setTax(double v){tax=v;}
}''')

w(md+'Employee.java', '''package com.example.gargstore.model;
import java.sql.Date;
public class Employee {
    private String employeeCode; private String name; private String designation; private String phoneNo; private Date dateOfJoining; private double salary; private String periodId;
    public String getEmployeeCode(){return employeeCode;} public void setEmployeeCode(String v){employeeCode=v;}
    public String getName(){return name;} public void setName(String v){name=v;}
    public String getDesignation(){return designation;} public void setDesignation(String v){designation=v;}
    public String getPhoneNo(){return phoneNo;} public void setPhoneNo(String v){phoneNo=v;}
    public Date getDateOfJoining(){return dateOfJoining;} public void setDateOfJoining(Date v){dateOfJoining=v;}
    public double getSalary(){return salary;} public void setSalary(double v){salary=v;}
    public String getPeriodId(){return periodId;} public void setPeriodId(String v){periodId=v;}
}''')

w(md+'SaleBill.java', '''package com.example.gargstore.model;
import java.sql.Date; import java.util.List;
public class SaleBill {
    private String billNo; private Date billDate; private String clientCode; private double totalAmount; private String paymentMode; private double balanceDue; private String periodId;
    private List<SaleBillItem> items;
    public String getBillNo(){return billNo;} public void setBillNo(String v){billNo=v;}
    public Date getBillDate(){return billDate;} public void setBillDate(Date v){billDate=v;}
    public String getClientCode(){return clientCode;} public void setClientCode(String v){clientCode=v;}
    public double getTotalAmount(){return totalAmount;} public void setTotalAmount(double v){totalAmount=v;}
    public String getPaymentMode(){return paymentMode;} public void setPaymentMode(String v){paymentMode=v;}
    public double getBalanceDue(){return balanceDue;} public void setBalanceDue(double v){balanceDue=v;}
    public String getPeriodId(){return periodId;} public void setPeriodId(String v){periodId=v;}
    public List<SaleBillItem> getItems(){return items;} public void setItems(List<SaleBillItem> v){items=v;}
}''')

w(md+'SaleBillItem.java', '''package com.example.gargstore.model;
public class SaleBillItem {
    private String billNo; private String itemCode; private int quantitySold; private double rateApplied; private double amount;
    public String getBillNo(){return billNo;} public void setBillNo(String v){billNo=v;}
    public String getItemCode(){return itemCode;} public void setItemCode(String v){itemCode=v;}
    public int getQuantitySold(){return quantitySold;} public void setQuantitySold(int v){quantitySold=v;}
    public double getRateApplied(){return rateApplied;} public void setRateApplied(double v){rateApplied=v;}
    public double getAmount(){return amount;} public void setAmount(double v){amount=v;}
}''')

w(md+'PurchaseBill.java', '''package com.example.gargstore.model;
import java.sql.Date; import java.util.List;
public class PurchaseBill {
    private String purchaseBillNo; private Date billDate; private String supplierCode; private double totalAmount; private double amountPaid; private double balanceDue; private String periodId;
    private List<PurchaseBillItem> items;
    public String getPurchaseBillNo(){return purchaseBillNo;} public void setPurchaseBillNo(String v){purchaseBillNo=v;}
    public Date getBillDate(){return billDate;} public void setBillDate(Date v){billDate=v;}
    public String getSupplierCode(){return supplierCode;} public void setSupplierCode(String v){supplierCode=v;}
    public double getTotalAmount(){return totalAmount;} public void setTotalAmount(double v){totalAmount=v;}
    public double getAmountPaid(){return amountPaid;} public void setAmountPaid(double v){amountPaid=v;}
    public double getBalanceDue(){return balanceDue;} public void setBalanceDue(double v){balanceDue=v;}
    public String getPeriodId(){return periodId;} public void setPeriodId(String v){periodId=v;}
    public List<PurchaseBillItem> getItems(){return items;} public void setItems(List<PurchaseBillItem> v){items=v;}
}''')

w(md+'PurchaseBillItem.java', '''package com.example.gargstore.model;
public class PurchaseBillItem {
    private String purchaseBillNo; private String itemCode; private int quantity; private double rate; private double amount;
    public String getPurchaseBillNo(){return purchaseBillNo;} public void setPurchaseBillNo(String v){purchaseBillNo=v;}
    public String getItemCode(){return itemCode;} public void setItemCode(String v){itemCode=v;}
    public int getQuantity(){return quantity;} public void setQuantity(int v){quantity=v;}
    public double getRate(){return rate;} public void setRate(double v){rate=v;}
    public double getAmount(){return amount;} public void setAmount(double v){amount=v;}
}''')

w(md+'PaymentReceived.java', '''package com.example.gargstore.model;
import java.sql.Date;
public class PaymentReceived {
    private String receiptNo; private String clientCode; private Date dateReceived; private double amountReceived; private String paymentMode;
    public String getReceiptNo(){return receiptNo;} public void setReceiptNo(String v){receiptNo=v;}
    public String getClientCode(){return clientCode;} public void setClientCode(String v){clientCode=v;}
    public Date getDateReceived(){return dateReceived;} public void setDateReceived(Date v){dateReceived=v;}
    public double getAmountReceived(){return amountReceived;} public void setAmountReceived(double v){amountReceived=v;}
    public String getPaymentMode(){return paymentMode;} public void setPaymentMode(String v){paymentMode=v;}
}''')

