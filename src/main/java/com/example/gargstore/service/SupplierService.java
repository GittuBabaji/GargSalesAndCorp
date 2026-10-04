package com.example.gargstore.service;
import com.example.gargstore.model.Supplier; import com.example.gargstore.repository.SupplierRepository; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Service; import java.util.List;
@Service
public class SupplierService {
    @Autowired private SupplierRepository repo;
    public List<Supplier> findAll() { return repo.findAll(); }
    public Supplier findById(String code) { return repo.findById(code); }
    public void save(Supplier s) { repo.save(s); }
    public void update(Supplier s) { repo.update(s); }
    public void delete(String code) { repo.delete(code); }
    public int count() { return repo.count(); }
}
