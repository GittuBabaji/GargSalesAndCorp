package com.example.gargstore.service;
import com.example.gargstore.model.*; import com.example.gargstore.repository.*; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Service; import org.springframework.transaction.annotation.Transactional; import java.util.List;
@Service
public class SaleBillService {
    @Autowired private SaleBillRepository saleRepo;
    @Autowired private StockItemRepository stockRepo;
    @Autowired private ClientRepository clientRepo;
    
    public List<SaleBill> findAll() { return saleRepo.findAll(); }
    public SaleBill findById(String code) { SaleBill s = saleRepo.findById(code); s.setItems(saleRepo.findItems(code)); return s; }
    
    @Transactional
    public void createSale(SaleBill bill, List<SaleBillItem> items) throws Exception {
        double total = 0;
        for(SaleBillItem item : items) {
            StockItem stock = stockRepo.findById(item.getItemCode());
            if(stock.getQuantity() < item.getQuantitySold()) throw new Exception("Insufficient stock for item: " + item.getItemCode());
            stock.setQuantity(stock.getQuantity() - item.getQuantitySold());
            stockRepo.update(stock);
            item.setBillNo(bill.getBillNo());
            total += item.getAmount();
        }
        bill.setTotalAmount(total);
        if("Credit".equals(bill.getPaymentMode())) { bill.setBalanceDue(total); }
        else { bill.setBalanceDue(0); }
        saleRepo.saveBill(bill);
        for(SaleBillItem item : items) { saleRepo.saveItem(item); }
        
        if(bill.getBalanceDue() > 0) {
            Client c = clientRepo.findById(bill.getClientCode());
            c.setDrBalance(c.getDrBalance() + bill.getBalanceDue());
            clientRepo.update(c);
        }
    }
}
