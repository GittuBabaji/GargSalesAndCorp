package com.example.gargstore.model;
import java.sql.Date;
public class Employee {
    private String employeeCode; private String name; private String designation; private String phoneNo; private Date dateOfJoining; private double salary;
    public String getEmployeeCode(){return employeeCode;} public void setEmployeeCode(String v){employeeCode=v;}
    public String getName(){return name;} public void setName(String v){name=v;}
    public String getDesignation(){return designation;} public void setDesignation(String v){designation=v;}
    public String getPhoneNo(){return phoneNo;} public void setPhoneNo(String v){phoneNo=v;}
    public Date getDateOfJoining(){return dateOfJoining;} public void setDateOfJoining(Date v){dateOfJoining=v;}
    public double getSalary(){return salary;} public void setSalary(double v){salary=v;}
}
