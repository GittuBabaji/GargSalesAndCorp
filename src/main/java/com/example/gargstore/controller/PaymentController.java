package com.example.gargstore.controller;

import com.example.gargstore.model.PaymentReceived;
import com.example.gargstore.service.PaymentReceivedService;
import com.example.gargstore.service.ClientService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/payments")
public class PaymentController {
    @Autowired private PaymentReceivedService payService;
    @Autowired private ClientService clientService;

    @GetMapping
    public String list(@RequestParam(defaultValue = "1") int page, Model m) {
        int pageSize = 25;
        int total = payService.count();
        int totalPages = Math.max(1, (int) Math.ceil((double) total / pageSize));
        if (page < 1) page = 1;
        if (page > totalPages && total > 0) page = totalPages;

        m.addAttribute("payments", payService.findPaged(page, pageSize));
        m.addAttribute("currentPage", page);
        m.addAttribute("totalPages", totalPages);
        m.addAttribute("totalRecords", total);
        m.addAttribute("pageSize", pageSize);
        return "payments/list";
    }

    @GetMapping("/new")
    public String showForm(Model m) {
        m.addAttribute("payment", new PaymentReceived());
        m.addAttribute("clients", clientService.findAll());
        return "payments/form";
    }

    @PostMapping
    public String save(PaymentReceived p) {
        payService.receivePayment(p);
        return "redirect:/payments";
    }
}
