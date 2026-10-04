package com.example.gargstore.service;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.example.gargstore.model.Supplier;
import com.example.gargstore.repository.SupplierRepository;

@Service
public class SupplierService {
    @Autowired
    private SupplierRepository repo;

    public List<Supplier> findAll() { return repo.findAll(); }
    public List<Supplier> findPagedWithSummary(int page, int size) { return repo.findPagedWithSummary(page, size); }
    public Supplier findById(String code) { return repo.findById(code); }
    public Supplier findByIdWithSummary(String code) { return repo.findByIdWithSummary(code); }
    public void save(Supplier s) { repo.save(s); }
    public void update(Supplier s) { repo.update(s); }
    public void delete(String code) { repo.delete(code); }
    public int count() { return repo.count(); }
    public double getTotalPurchases() { return repo.getTotalPurchases(); }
    public double getTotalPaid() { return repo.getTotalPaid(); }
    public double getTotalBalanceDue() { return repo.getTotalBalanceDue(); }
}
