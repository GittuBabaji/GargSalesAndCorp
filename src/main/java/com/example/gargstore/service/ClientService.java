package com.example.gargstore.service;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.example.gargstore.model.Client;
import com.example.gargstore.repository.ClientRepository;

@Service
public class ClientService {
    @Autowired
    private ClientRepository repo;

    public List<Client> findAll() {
        return repo.findAll();
    }

    public List<Client> findPagedWithSummary(int page, int size) {
        return repo.findPagedWithSummary(page, size);
    }

    public Client findById(String code) {
        return repo.findById(code);
    }

    public Client findByIdWithSummary(String code) {
        return repo.findByIdWithSummary(code);
    }

    public void save(Client c) {
        repo.save(c);
    }

    public void update(Client c) {
        repo.update(c);
    }

    public void delete(String code) {
        repo.delete(code);
    }

    public int count() {
        return repo.count();
    }

    public double getTotalSales() {
        return repo.getTotalSales();
    }

    public double getTotalPayments() {
        return repo.getTotalPayments();
    }

    public double getTotalBalanceDue() {
        return repo.getTotalBalanceDue();
    }

    public double getTotalDrBalance() {
        return repo.getTotalDrBalance();
    }

    public double getTotalCrBalance() {
        return repo.getTotalCrBalance();
    }
}
