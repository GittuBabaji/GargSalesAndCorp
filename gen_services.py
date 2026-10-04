import os
def w(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
sv = 'C:/Users/Asus/OneDrive/Desktop/khatta/garg-store/src/main/java/com/example/gargstore/service/'

w(sv+'ClientService.java', '''package com.example.gargstore.service;
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
}''')

w(sv+'SupplierService.java', '''package com.example.gargstore.service;
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
}''')

w(sv+'StockItemService.java', '''package com.example.gargstore.service;
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
}''')

w(sv+'SaleBillService.java', '''package com.example.gargstore.service;
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
}''')

w(sv+'PurchaseBillService.java', '''package com.example.gargstore.service;
import com.example.gargstore.model.*; import com.example.gargstore.repository.*; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Service; import org.springframework.transaction.annotation.Transactional; import java.util.List;
@Service
public class PurchaseBillService {
    @Autowired private PurchaseBillRepository purRepo;
    @Autowired private StockItemRepository stockRepo;
    
    public List<PurchaseBill> findAll() { return purRepo.findAll(); }
    public PurchaseBill findById(String code) { PurchaseBill p = purRepo.findById(code); p.setItems(purRepo.findItems(code)); return p; }
    
    @Transactional
    public void createPurchase(PurchaseBill bill, List<PurchaseBillItem> items) {
        double total = 0;
        for(PurchaseBillItem item : items) {
            StockItem stock = stockRepo.findById(item.getItemCode());
            stock.setQuantity(stock.getQuantity() + item.getQuantity());
            stockRepo.update(stock);
            item.setPurchaseBillNo(bill.getPurchaseBillNo());
            total += item.getAmount();
        }
        bill.setTotalAmount(total);
        bill.setBalanceDue(total - bill.getAmountPaid());
        purRepo.saveBill(bill);
        for(PurchaseBillItem item : items) { purRepo.saveItem(item); }
    }
}''')

w(sv+'PaymentReceivedService.java', '''package com.example.gargstore.service;
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
}''')

w(sv+'EmployeeService.java', '''package com.example.gargstore.service;
import com.example.gargstore.model.Employee; import com.example.gargstore.repository.EmployeeRepository; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Service; import java.util.List;
@Service
public class EmployeeService {
    @Autowired private EmployeeRepository repo;
    public List<Employee> findAll() { return repo.findAll(); }
    public int count() { return repo.count(); }
}''')

w(sv+'FinancialSummaryService.java', '''package com.example.gargstore.service;
import com.example.gargstore.model.FinancialSummary; import com.example.gargstore.repository.FinancialSummaryRepository; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Service; import java.util.List;
@Service
public class FinancialSummaryService {
    @Autowired private FinancialSummaryRepository repo;
    public List<FinancialSummary> findAll() { return repo.findAll(); }
}''')

