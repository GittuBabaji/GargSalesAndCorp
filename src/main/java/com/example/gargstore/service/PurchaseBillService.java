package com.example.gargstore.service;

import com.example.gargstore.model.*;
import com.example.gargstore.repository.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;

@Service
public class PurchaseBillService {
    @Autowired private PurchaseBillRepository purRepo;
    @Autowired private StockItemRepository stockRepo;

    public List<PurchaseBill> findAll() { return purRepo.findAll(); }
    public List<PurchaseBill> findPaged(int page, int size) { return purRepo.findPaged(page, size); }
    public List<PurchaseBill> findBySupplierCode(String supplierCode) { return purRepo.findBySupplierCode(supplierCode); }
    public int count() { return purRepo.count(); }

    public PurchaseBill findById(String code) {
        PurchaseBill p = purRepo.findById(code);
        if (p != null) {
            p.setItems(purRepo.findItems(code));
        }
        return p;
    }

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
}
