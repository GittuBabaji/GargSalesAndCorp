package com.example.gargstore.service;

import com.example.gargstore.model.Employee;
import com.example.gargstore.repository.EmployeeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class EmployeeService {
    @Autowired private EmployeeRepository repo;
    public List<Employee> findAll() { return repo.findAll(); }
    public List<Employee> findPaged(int page, int size) { return repo.findPaged(page, size); }
    public int count() { return repo.count(); }
}
