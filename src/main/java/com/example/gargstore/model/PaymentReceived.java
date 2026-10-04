package com.example.gargstore.model;
import java.sql.Date;
public class PaymentReceived {
    private String receiptNo; private String clientCode; private Date dateReceived; private double amountReceived; private String paymentMode;
    public String getReceiptNo(){return receiptNo;} public void setReceiptNo(String v){receiptNo=v;}
    public String getClientCode(){return clientCode;} public void setClientCode(String v){clientCode=v;}
    public Date getDateReceived(){return dateReceived;} public void setDateReceived(Date v){dateReceived=v;}
    public double getAmountReceived(){return amountReceived;} public void setAmountReceived(double v){amountReceived=v;}
    public String getPaymentMode(){return paymentMode;} public void setPaymentMode(String v){paymentMode=v;}
}
