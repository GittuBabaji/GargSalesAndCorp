package com.example.gargstore.repository;

import com.example.gargstore.model.FinancialSummary;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public class FinancialSummaryRepository {
    @Autowired
    private JdbcTemplate jdbc;
    private RowMapper<FinancialSummary> mapper = (rs, rowNum) -> {
        FinancialSummary f = new FinancialSummary();
        f.setPeriodId(rs.getString("Period_Id"));
        f.setPeriod(rs.getString("Period"));
        f.setTotalAssets(rs.getDouble("Total_Assets"));
        f.setTotalLiabilities(rs.getDouble("Total_Liabilities"));
        f.setOperatingCost(rs.getDouble("Operating_Cost"));
        f.setGrossProfit(rs.getDouble("Gross_Profit"));
        f.setNetProfit(rs.getDouble("Net_Profit"));
        f.setTax(rs.getDouble("Tax"));
        return f;
    };

    public List<FinancialSummary> findAll() {
        return jdbc.query("SELECT * FROM Financial_Summary", mapper);
    }

    public FinancialSummary findById(String id) {
        return jdbc.queryForObject("SELECT * FROM Financial_Summary WHERE Period_Id=?", mapper, id);
    }
}
