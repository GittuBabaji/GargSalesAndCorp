package com.example.gargstore.model;

public class Client {
    private String clientCode;
    private String name;
    private String address;
    private String locality;
    private String phoneNo;
    private String gstNo;
    private double drBalance;
    private double crBalance;

    // Summary metrics per client
    private double totalSales;
    private int totalBills;
    private double totalPaid;
    private double totalDue;

    public String getClientCode() {
        return clientCode;
    }

    public void setClientCode(String c) {
        clientCode = c;
    }

    public String getName() {
        return name;
    }

    public void setName(String n) {
        name = n;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String a) {
        address = a;
    }

    public String getLocality() {
        return locality;
    }

    public void setLocality(String l) {
        locality = l;
    }

    public String getPhoneNo() {
        return phoneNo;
    }

    public void setPhoneNo(String p) {
        phoneNo = p;
    }

    public String getGstNo() {
        return gstNo;
    }

    public void setGstNo(String g) {
        gstNo = g;
    }

    public double getDrBalance() {
        return drBalance;
    }

    public void setDrBalance(double d) {
        drBalance = d;
    }

    public double getCrBalance() {
        return crBalance;
    }

    public void setCrBalance(double c) {
        crBalance = c;
    }

    public double getTotalSales() {
        return totalSales;
    }

    public void setTotalSales(double totalSales) {
        this.totalSales = totalSales;
    }

    public int getTotalBills() {
        return totalBills;
    }

    public void setTotalBills(int totalBills) {
        this.totalBills = totalBills;
    }

    public double getTotalPaid() {
        return totalPaid;
    }

    public void setTotalPaid(double totalPaid) {
        this.totalPaid = totalPaid;
    }

    public double getTotalDue() {
        return totalDue;
    }

    public void setTotalDue(double totalDue) {
        this.totalDue = totalDue;
    }
}
