package com.example.gargstore.model;
public class Client {
    private String clientCode; private String name; private String address; private String locality; private String phoneNo; private String gstNo; private double drBalance; private double crBalance;
    // getters and setters
    public String getClientCode(){return clientCode;} public void setClientCode(String c){clientCode=c;}
    public String getName(){return name;} public void setName(String n){name=n;}
    public String getAddress(){return address;} public void setAddress(String a){address=a;}
    public String getLocality(){return locality;} public void setLocality(String l){locality=l;}
    public String getPhoneNo(){return phoneNo;} public void setPhoneNo(String p){phoneNo=p;}
    public String getGstNo(){return gstNo;} public void setGstNo(String g){gstNo=g;}
    public double getDrBalance(){return drBalance;} public void setDrBalance(double d){drBalance=d;}
    public double getCrBalance(){return crBalance;} public void setCrBalance(double c){crBalance=c;}
}
