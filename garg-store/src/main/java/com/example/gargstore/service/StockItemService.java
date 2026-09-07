package com.example.gargstore.service;
import com.example.gargstore.model.StockItem; import com.example.gargstore.repository.StockItemRepository; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Service; import java.util.List;
@Service
public class StockItemService {
    @Autowired private StockItemRepository repo;
    public List<StockItem> findAll() { return repo.findAll(); }
    public List<StockItem> findLowStock() { return repo.findLowStock(); }
    public StockItem findById(String code) { return repo.findById(code); }
    public void save(StockItem s) { repo.save(s); }
    public void update(StockItem s) { repo.update(s); }
    public void delete(String code) { repo.delete(code); }
    public int count() { return repo.count(); }
}
