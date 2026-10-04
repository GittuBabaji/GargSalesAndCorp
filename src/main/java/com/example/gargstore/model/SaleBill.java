package com.example.gargstore.model;
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
}
