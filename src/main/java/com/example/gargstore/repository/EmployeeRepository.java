package com.example.gargstore.repository;

import com.example.gargstore.model.Employee;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public class EmployeeRepository {
    @Autowired private JdbcTemplate jdbc;

    private RowMapper<Employee> mapper = (rs, rowNum) -> {
        Employee e = new Employee();
        e.setEmployeeCode(rs.getString("Employee_Code"));
        e.setName(rs.getString("Name"));
        e.setDesignation(rs.getString("Designation"));
        e.setPhoneNo(rs.getString("Phone_No"));
        e.setDateOfJoining(rs.getDate("Date_of_Joining"));
        e.setSalary(rs.getDouble("Salary"));
        return e;
    };

    public List<Employee> findAll() {
        return jdbc.query("SELECT * FROM Employee ORDER BY Employee_Code", mapper);
    }

    public List<Employee> findPaged(int page, int size) {
        int offset = Math.max(0, (page - 1) * size);
        return jdbc.query("SELECT * FROM Employee ORDER BY Employee_Code LIMIT ? OFFSET ?", mapper, size, offset);
    }

    public Employee findById(String id) {
        return jdbc.queryForObject("SELECT * FROM Employee WHERE Employee_Code=?", mapper, id);
    }

    public int count() {
        Integer c = jdbc.queryForObject("SELECT COUNT(*) FROM Employee", Integer.class);
        return c == null ? 0 : c;
    }
}
