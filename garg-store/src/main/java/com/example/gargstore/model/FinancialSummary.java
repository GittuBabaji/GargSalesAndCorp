package com.example.gargstore.model;
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
}
