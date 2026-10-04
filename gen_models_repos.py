import os
def w(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
base = 'C:/Users/Asus/OneDrive/Desktop/khatta/garg-store/'
md = base + 'src/main/java/com/example/gargstore/model/'
rp = base + 'src/main/java/com/example/gargstore/repository/'

w(md+'Client.java', '''package com.example.gargstore.model;
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
}''')

w(md+'Supplier.java', '''package com.example.gargstore.model;
public class Supplier {
    private String supplierCode; private String name; private String address; private String locality; private String phoneNo; private String gstNo;
    public String getSupplierCode(){return supplierCode;} public void setSupplierCode(String s){supplierCode=s;}
    public String getName(){return name;} public void setName(String n){name=n;}
    public String getAddress(){return address;} public void setAddress(String a){address=a;}
    public String getLocality(){return locality;} public void setLocality(String l){locality=l;}
    public String getPhoneNo(){return phoneNo;} public void setPhoneNo(String p){phoneNo=p;}
    public String getGstNo(){return gstNo;} public void setGstNo(String g){gstNo=g;}
}''')

w(md+'StockItem.java', '''package com.example.gargstore.model;
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
}''')

w(rp+'ClientRepository.java', '''package com.example.gargstore.repository;
import com.example.gargstore.model.Client; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.jdbc.core.JdbcTemplate; import org.springframework.jdbc.core.RowMapper; import org.springframework.stereotype.Repository; import java.sql.ResultSet; import java.sql.SQLException; import java.util.List;
@Repository
public class ClientRepository {
    @Autowired private JdbcTemplate jdbc;
    private RowMapper<Client> mapper = (rs, rowNum) -> {
        Client c = new Client(); c.setClientCode(rs.getString("Client_Code")); c.setName(rs.getString("Name")); c.setAddress(rs.getString("Address")); c.setLocality(rs.getString("Locality")); c.setPhoneNo(rs.getString("Phone_No")); c.setGstNo(rs.getString("GST_No")); c.setDrBalance(rs.getDouble("DR_Balance")); c.setCrBalance(rs.getDouble("CR_Balance")); return c;
    };
    public List<Client> findAll() { return jdbc.query("SELECT * FROM Client", mapper); }
    public Client findById(String code) { return jdbc.queryForObject("SELECT * FROM Client WHERE Client_Code = ?", mapper, code); }
    public int save(Client c) { return jdbc.update("INSERT INTO Client (Client_Code, Name, Address, Locality, Phone_No, GST_No, DR_Balance, CR_Balance) VALUES (?,?,?,?,?,?,?,?)", c.getClientCode(), c.getName(), c.getAddress(), c.getLocality(), c.getPhoneNo(), c.getGstNo(), c.getDrBalance(), c.getCrBalance()); }
    public int update(Client c) { return jdbc.update("UPDATE Client SET Name=?, Address=?, Locality=?, Phone_No=?, GST_No=?, DR_Balance=?, CR_Balance=? WHERE Client_Code=?", c.getName(), c.getAddress(), c.getLocality(), c.getPhoneNo(), c.getGstNo(), c.getDrBalance(), c.getCrBalance(), c.getClientCode()); }
    public int delete(String code) { return jdbc.update("DELETE FROM Client WHERE Client_Code=?", code); }
    public int count() { return jdbc.queryForObject("SELECT COUNT(*) FROM Client", Integer.class); }
}''')

w(rp+'SupplierRepository.java', '''package com.example.gargstore.repository;
import com.example.gargstore.model.Supplier; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.jdbc.core.JdbcTemplate; import org.springframework.jdbc.core.RowMapper; import org.springframework.stereotype.Repository; import java.util.List;
@Repository
public class SupplierRepository {
    @Autowired private JdbcTemplate jdbc;
    private RowMapper<Supplier> mapper = (rs, rowNum) -> {
        Supplier s = new Supplier(); s.setSupplierCode(rs.getString("Supplier_Code")); s.setName(rs.getString("Name")); s.setAddress(rs.getString("Address")); s.setLocality(rs.getString("Locality")); s.setPhoneNo(rs.getString("Phone_No")); s.setGstNo(rs.getString("GST_No")); return s;
    };
    public List<Supplier> findAll() { return jdbc.query("SELECT * FROM Supplier", mapper); }
    public Supplier findById(String code) { return jdbc.queryForObject("SELECT * FROM Supplier WHERE Supplier_Code = ?", mapper, code); }
    public int save(Supplier s) { return jdbc.update("INSERT INTO Supplier (Supplier_Code, Name, Address, Locality, Phone_No, GST_No) VALUES (?,?,?,?,?,?)", s.getSupplierCode(), s.getName(), s.getAddress(), s.getLocality(), s.getPhoneNo(), s.getGstNo()); }
    public int update(Supplier s) { return jdbc.update("UPDATE Supplier SET Name=?, Address=?, Locality=?, Phone_No=?, GST_No=? WHERE Supplier_Code=?", s.getName(), s.getAddress(), s.getLocality(), s.getPhoneNo(), s.getGstNo(), s.getSupplierCode()); }
    public int delete(String code) { return jdbc.update("DELETE FROM Supplier WHERE Supplier_Code=?", code); }
    public int count() { return jdbc.queryForObject("SELECT COUNT(*) FROM Supplier", Integer.class); }
}''')

w(rp+'StockItemRepository.java', '''package com.example.gargstore.repository;
import com.example.gargstore.model.StockItem; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.jdbc.core.JdbcTemplate; import org.springframework.jdbc.core.RowMapper; import org.springframework.stereotype.Repository; import java.util.List;
@Repository
public class StockItemRepository {
    @Autowired private JdbcTemplate jdbc;
    private RowMapper<StockItem> mapper = (rs, rowNum) -> {
        StockItem s = new StockItem(); s.setItemCode(rs.getString("Item_Code")); s.setItemName(rs.getString("Item_Name")); s.setCategory(rs.getString("Category")); s.setUnit(rs.getString("Unit")); s.setQuantity(rs.getInt("Quantity")); s.setCostPrice(rs.getDouble("Cost_Price")); s.setSellingPrice(rs.getDouble("Selling_Price")); s.setReorderLevel(rs.getInt("Reorder_Level")); return s;
    };
    public List<StockItem> findAll() { return jdbc.query("SELECT * FROM Stock_Item", mapper); }
    public List<StockItem> findLowStock() { return jdbc.query("SELECT * FROM Stock_Item WHERE Quantity <= Reorder_Level", mapper); }
    public StockItem findById(String code) { return jdbc.queryForObject("SELECT * FROM Stock_Item WHERE Item_Code = ?", mapper, code); }
    public int save(StockItem s) { return jdbc.update("INSERT INTO Stock_Item (Item_Code, Item_Name, Category, Unit, Quantity, Cost_Price, Selling_Price, Reorder_Level) VALUES (?,?,?,?,?,?,?,?)", s.getItemCode(), s.getItemName(), s.getCategory(), s.getUnit(), s.getQuantity(), s.getCostPrice(), s.getSellingPrice(), s.getReorderLevel()); }
    public int update(StockItem s) { return jdbc.update("UPDATE Stock_Item SET Item_Name=?, Category=?, Unit=?, Quantity=?, Cost_Price=?, Selling_Price=?, Reorder_Level=? WHERE Item_Code=?", s.getItemName(), s.getCategory(), s.getUnit(), s.getQuantity(), s.getCostPrice(), s.getSellingPrice(), s.getReorderLevel(), s.getItemCode()); }
    public int delete(String code) { return jdbc.update("DELETE FROM Stock_Item WHERE Item_Code=?", code); }
    public int count() { return jdbc.queryForObject("SELECT COUNT(*) FROM Stock_Item", Integer.class); }
}''')
