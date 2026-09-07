package com.example.gargstore.repository;
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
}
