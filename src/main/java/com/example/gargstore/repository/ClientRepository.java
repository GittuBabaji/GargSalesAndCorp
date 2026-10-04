package com.example.gargstore.repository;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import com.example.gargstore.model.Client;

@Repository
public class ClientRepository {
    @Autowired
    private JdbcTemplate jdbc;
    private RowMapper<Client> mapper = (rs, rowNum) -> {
        Client c = new Client();
        c.setClientCode(rs.getString("Client_Code"));
        c.setName(rs.getString("Name"));
        c.setAddress(rs.getString("Address"));
        c.setLocality(rs.getString("Locality"));
        c.setPhoneNo(rs.getString("Phone_No"));
        c.setGstNo(rs.getString("GST_No"));
        c.setDrBalance(rs.getDouble("DR_Balance"));
        c.setCrBalance(rs.getDouble("CR_Balance"));
        return c;
    };

    public List<Client> findAll() {
        return jdbc.query("SELECT * FROM Client", mapper);
    }

    public Client findById(String code) {
        return jdbc.queryForObject("SELECT * FROM Client WHERE Client_Code = ?", mapper, code);
    }

    public int save(Client c) {
        return jdbc.update(
                "INSERT INTO Client (Client_Code, Name, Address, Locality, Phone_No, GST_No, DR_Balance, CR_Balance) VALUES (?,?,?,?,?,?,?,?)",
                c.getClientCode(), c.getName(), c.getAddress(), c.getLocality(), c.getPhoneNo(), c.getGstNo(),
                c.getDrBalance(), c.getCrBalance());
    }

    public int update(Client c) {
        return jdbc.update(
                "UPDATE Client SET Name=?, Address=?, Locality=?, Phone_No=?, GST_No=?, DR_Balance=?, CR_Balance=? WHERE Client_Code=?",
                c.getName(), c.getAddress(), c.getLocality(), c.getPhoneNo(), c.getGstNo(), c.getDrBalance(),
                c.getCrBalance(), c.getClientCode());
    }

    public int delete(String code) {
        return jdbc.update("DELETE FROM Client WHERE Client_Code=?", code);
    }

    public int count() {
        return jdbc.queryForObject("SELECT COUNT(*) FROM Client", Integer.class);
    }
}
