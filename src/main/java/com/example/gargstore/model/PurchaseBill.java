package com.example.gargstore.model;
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
}
