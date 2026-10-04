package com.example.gargstore.repository;

import com.example.gargstore.model.StockItem;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public class StockItemRepository {
    @Autowired private JdbcTemplate jdbc;

    private RowMapper<StockItem> mapper = (rs, rowNum) -> {
        StockItem s = new StockItem();
        s.setItemCode(rs.getString("Item_Code"));
        s.setItemName(rs.getString("Item_Name"));
        s.setCategory(rs.getString("Category"));
        s.setUnit(rs.getString("Unit"));
        s.setQuantity(rs.getInt("Quantity"));
        s.setCostPrice(rs.getDouble("Cost_Price"));
        s.setSellingPrice(rs.getDouble("Selling_Price"));
        s.setReorderLevel(rs.getInt("Reorder_Level"));
        return s;
    };

    public List<StockItem> findAll() {
        return jdbc.query("SELECT * FROM Stock_Item ORDER BY Item_Code", mapper);
    }

    public List<StockItem> findPaged(int page, int size) {
        int offset = Math.max(0, (page - 1) * size);
        return jdbc.query("SELECT * FROM Stock_Item ORDER BY Item_Code LIMIT ? OFFSET ?", mapper, size, offset);
    }

    public List<StockItem> findLowStock() {
        return jdbc.query("SELECT * FROM Stock_Item WHERE Quantity <= Reorder_Level ORDER BY Item_Code", mapper);
    }

    public StockItem findById(String code) {
        return jdbc.queryForObject("SELECT * FROM Stock_Item WHERE Item_Code = ?", mapper, code);
    }

    public int save(StockItem s) {
        return jdbc.update("INSERT INTO Stock_Item (Item_Code, Item_Name, Category, Unit, Quantity, Cost_Price, Selling_Price, Reorder_Level) VALUES (?,?,?,?,?,?,?,?)",
                s.getItemCode(), s.getItemName(), s.getCategory(), s.getUnit(), s.getQuantity(), s.getCostPrice(), s.getSellingPrice(), s.getReorderLevel());
    }

    public int update(StockItem s) {
        return jdbc.update("UPDATE Stock_Item SET Item_Name=?, Category=?, Unit=?, Quantity=?, Cost_Price=?, Selling_Price=?, Reorder_Level=? WHERE Item_Code=?",
                s.getItemName(), s.getCategory(), s.getUnit(), s.getQuantity(), s.getCostPrice(), s.getSellingPrice(), s.getReorderLevel(), s.getItemCode());
    }

    public int delete(String code) {
        return jdbc.update("DELETE FROM Stock_Item WHERE Item_Code=?", code);
    }

    public int count() {
        Integer c = jdbc.queryForObject("SELECT COUNT(*) FROM Stock_Item", Integer.class);
        return c == null ? 0 : c;
    }
}
