package com.example.gargstore.model;
public class StockItem {
    private String itemCode; private String itemName; private String category; private String unit; private int quantity; private double costPrice; private double sellingPrice; private int reorderLevel;
    public String getItemCode(){return itemCode;} public void setItemCode(String i){itemCode=i;}
    public String getItemName(){return itemName;} public void setItemName(String i){itemName=i;}
    public String getCategory(){return category;} public void setCategory(String c){category=c;}
    public String getUnit(){return unit;} public void setUnit(String u){unit=u;}
    public int getQuantity(){return quantity;} public void setQuantity(int q){quantity=q;}
    public double getCostPrice(){return costPrice;} public void setCostPrice(double c){costPrice=c;}
    public double getSellingPrice(){return sellingPrice;} public void setSellingPrice(double s){sellingPrice=s;}
    public int getReorderLevel(){return reorderLevel;} public void setReorderLevel(int r){reorderLevel=r;}
}
