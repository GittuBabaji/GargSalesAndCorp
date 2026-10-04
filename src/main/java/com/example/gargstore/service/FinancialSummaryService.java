package com.example.gargstore.service;
import com.example.gargstore.model.FinancialSummary; import com.example.gargstore.repository.FinancialSummaryRepository; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Service; import java.util.List;
@Service
public class FinancialSummaryService {
    @Autowired private FinancialSummaryRepository repo;
    public List<FinancialSummary> findAll() { return repo.findAll(); }
}
