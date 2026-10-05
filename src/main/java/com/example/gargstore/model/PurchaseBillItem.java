package com.example.gargstore.model;

public class PurchaseBillItem {
    private String purchaseBillNo;
    private String itemCode;
    private int quantity;
    private double rate;
    private double amount;

    public String getPurchaseBillNo() {
        return purchaseBillNo;
    }

    public void setPurchaseBillNo(String v) {
        purchaseBillNo = v;
    }

    public String getItemCode() {
        return itemCode;
    }

    public void setItemCode(String v) {
        itemCode = v;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int v) {
        quantity = v;
    }

    public double getRate() {
        return rate;
    }

    public void setRate(double v) {
        rate = v;
    }

    public double getAmount() {
        return amount;
    }

    public void setAmount(double v) {
        amount = v;
    }
}
