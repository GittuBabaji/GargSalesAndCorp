package com.example.gargstore.service;
import com.example.gargstore.model.*; import com.example.gargstore.repository.*; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Service; import org.springframework.transaction.annotation.Transactional; import java.util.List;
@Service
public class PaymentReceivedService {
    @Autowired private PaymentReceivedRepository payRepo;
    @Autowired private ClientRepository clientRepo;
    public List<PaymentReceived> findAll() { return payRepo.findAll(); }
    
    @Transactional
    public void receivePayment(PaymentReceived pay) {
        payRepo.save(pay);
        Client c = clientRepo.findById(pay.getClientCode());
        c.setDrBalance(Math.max(0, c.getDrBalance() - pay.getAmountReceived()));
        clientRepo.update(c);
    }
}
