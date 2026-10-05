package com.example.gargstore.model;

public class SaleBillItem {
    private String billNo;
    private String itemCode;
    private int quantitySold;
    private double rateApplied;
    private double amount;

    public String getBillNo() {
        return billNo;
    }

    public void setBillNo(String v) {
        billNo = v;
    }

    public String getItemCode() {
        return itemCode;
    }

    public void setItemCode(String v) {
        itemCode = v;
    }

    public int getQuantitySold() {
        return quantitySold;
    }

    public void setQuantitySold(int v) {
        quantitySold = v;
    }

    public double getRateApplied() {
        return rateApplied;
    }

    public void setRateApplied(double v) {
        rateApplied = v;
    }

    public double getAmount() {
        return amount;
    }

    public void setAmount(double v) {
        amount = v;
    }
}
