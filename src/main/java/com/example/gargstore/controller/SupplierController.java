package com.example.gargstore.controller;

import com.example.gargstore.model.PurchaseBill;
import com.example.gargstore.model.Supplier;
import com.example.gargstore.service.PurchaseBillService;
import com.example.gargstore.service.SupplierService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@Controller
@RequestMapping("/suppliers")
public class SupplierController {
    @Autowired private SupplierService service;
    @Autowired private PurchaseBillService purchaseService;

    @GetMapping
    public String list(@RequestParam(defaultValue = "1") int page, Model m) {
        int pageSize = 25;
        int total = service.count();
        int totalPages = Math.max(1, (int) Math.ceil((double) total / pageSize));
        if (page < 1) page = 1;
        if (page > totalPages && total > 0) page = totalPages;

        m.addAttribute("suppliers", service.findPagedWithSummary(page, pageSize));
        m.addAttribute("currentPage", page);
        m.addAttribute("totalPages", totalPages);
        m.addAttribute("totalRecords", total);
        m.addAttribute("pageSize", pageSize);

        // Overall summary per supplier segment
        m.addAttribute("totalPurchases", service.getTotalPurchases());
        m.addAttribute("totalPaid", service.getTotalPaid());
        m.addAttribute("totalDue", service.getTotalBalanceDue());

        return "suppliers/list";
    }

    @GetMapping({"/view/{code}", "/{code}"})
    public String view(@PathVariable String code, Model m) {
        Supplier supplier = service.findByIdWithSummary(code);
        List<PurchaseBill> purchases = purchaseService.findBySupplierCode(code);

        m.addAttribute("supplier", supplier);
        m.addAttribute("purchases", purchases);
        return "suppliers/view";
    }

    @GetMapping("/new")
    public String showForm(Model m) {
        m.addAttribute("supplier", new Supplier());
        return "suppliers/form";
    }

    @PostMapping
    public String save(@ModelAttribute Supplier s) {
        service.save(s);
        return "redirect:/suppliers";
    }

    @GetMapping("/edit/{code}")
    public String edit(@PathVariable String code, Model m) {
        m.addAttribute("supplier", service.findById(code));
        return "suppliers/form";
    }

    @PostMapping("/update/{code}")
    public String update(@PathVariable String code, @ModelAttribute Supplier s) {
        s.setSupplierCode(code);
        service.update(s);
        return "redirect:/suppliers";
    }

    @PostMapping("/delete/{code}")
    public String delete(@PathVariable String code) {
        try {
            service.delete(code);
            return "redirect:/suppliers?success=Supplier+" + code + "+deleted+successfully";
        } catch (Exception e) {
            return "redirect:/suppliers?error=Cannot+delete+supplier+" + code + ":+supplier+has+associated+bills.";
        }
    }
}
