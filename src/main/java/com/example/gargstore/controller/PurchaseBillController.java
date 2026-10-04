package com.example.gargstore.controller;

import com.example.gargstore.model.*;
import com.example.gargstore.service.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import java.util.ArrayList;
import java.util.List;

@Controller
@RequestMapping("/purchases")
public class PurchaseBillController {
    @Autowired private PurchaseBillService purService;
    @Autowired private SupplierService supService;
    @Autowired private StockItemService stockService;
    @Autowired private FinancialSummaryService finService;

    @GetMapping
    public String list(@RequestParam(defaultValue = "1") int page, Model m) {
        int pageSize = 25;
        int total = purService.count();
        int totalPages = Math.max(1, (int) Math.ceil((double) total / pageSize));
        if (page < 1) page = 1;
        if (page > totalPages && total > 0) page = totalPages;

        m.addAttribute("purchases", purService.findPaged(page, pageSize));
        m.addAttribute("currentPage", page);
        m.addAttribute("totalPages", totalPages);
        m.addAttribute("totalRecords", total);
        m.addAttribute("pageSize", pageSize);
        return "purchases/list";
    }

    @GetMapping("/new")
    public String showForm(Model m) {
        m.addAttribute("purchase", new PurchaseBill());
        m.addAttribute("suppliers", supService.findAll());
        m.addAttribute("items", stockService.findAll());
        m.addAttribute("summaries", finService.findAll());
        return "purchases/form";
    }

    @PostMapping
    public String save(PurchaseBill purchase, String[] itemCode, int[] quantity, double[] rate) {
        if (purchase.getPeriodId() != null && purchase.getPeriodId().trim().isEmpty()) {
            purchase.setPeriodId(null);
        }
        List<PurchaseBillItem> items = new ArrayList<>();
        for (int i = 0; i < itemCode.length; i++) {
            if (itemCode[i] != null && !itemCode[i].isEmpty()) {
                PurchaseBillItem it = new PurchaseBillItem();
                it.setItemCode(itemCode[i]);
                it.setQuantity(quantity[i]);
                it.setRate(rate[i]);
                it.setAmount(quantity[i] * rate[i]);
                items.add(it);
            }
        }
        purService.createPurchase(purchase, items);
        return "redirect:/purchases";
    }

    @GetMapping("/{billNo}")
    public String view(@PathVariable String billNo, Model m) {
        m.addAttribute("purchase", purService.findById(billNo));
        return "purchases/view";
    }
}
