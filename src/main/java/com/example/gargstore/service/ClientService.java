package com.example.gargstore.service;
import com.example.gargstore.model.Client; import com.example.gargstore.repository.ClientRepository; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Service; import java.util.List;
@Service
public class ClientService {
    @Autowired private ClientRepository repo;
    public List<Client> findAll() { return repo.findAll(); }
    public Client findById(String code) { return repo.findById(code); }
    public void save(Client c) { repo.save(c); }
    public void update(Client c) { repo.update(c); }
    public void delete(String code) { repo.delete(code); }
    public int count() { return repo.count(); }
}
