package com.example.gargstore.model;

public class Supplier {
    private String supplierCode;
    private String name;
    private String address;
    private String locality;
    private String phoneNo;
    private String gstNo;

    // Summary metrics per supplier
    private double totalPurchases;
    private int totalBills;
    private double totalPaid;
    private double totalDue;

    public String getSupplierCode() { return supplierCode; }
    public void setSupplierCode(String s) { supplierCode = s; }

    public String getName() { return name; }
    public void setName(String n) { name = n; }

    public String getAddress() { return address; }
    public void setAddress(String a) { address = a; }

    public String getLocality() { return locality; }
    public void setLocality(String l) { locality = l; }

    public String getPhoneNo() { return phoneNo; }
    public void setPhoneNo(String p) { phoneNo = p; }

    public String getGstNo() { return gstNo; }
    public void setGstNo(String g) { gstNo = g; }

    public double getTotalPurchases() { return totalPurchases; }
    public void setTotalPurchases(double totalPurchases) { this.totalPurchases = totalPurchases; }

    public int getTotalBills() { return totalBills; }
    public void setTotalBills(int totalBills) { this.totalBills = totalBills; }

    public double getTotalPaid() { return totalPaid; }
    public void setTotalPaid(double totalPaid) { this.totalPaid = totalPaid; }

    public double getTotalDue() { return totalDue; }
    public void setTotalDue(double totalDue) { this.totalDue = totalDue; }
}
