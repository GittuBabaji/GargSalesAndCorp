package com.example.gargstore.controller;

import com.example.gargstore.model.Client;
import com.example.gargstore.model.PaymentReceived;
import com.example.gargstore.model.SaleBill;
import com.example.gargstore.service.ClientService;
import com.example.gargstore.service.PaymentReceivedService;
import com.example.gargstore.service.SaleBillService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@Controller
@RequestMapping("/clients")
public class ClientController {
    @Autowired private ClientService service;
    @Autowired private SaleBillService saleService;
    @Autowired private PaymentReceivedService paymentService;

    @GetMapping
    public String list(@RequestParam(defaultValue = "1") int page, Model m) {
        int pageSize = 25;
        int total = service.count();
        int totalPages = Math.max(1, (int) Math.ceil((double) total / pageSize));
        if (page < 1) page = 1;
        if (page > totalPages && total > 0) page = totalPages;

        m.addAttribute("clients", service.findPagedWithSummary(page, pageSize));
        m.addAttribute("currentPage", page);
        m.addAttribute("totalPages", totalPages);
        m.addAttribute("totalRecords", total);
        m.addAttribute("pageSize", pageSize);

        // Overall client financial summaries
        m.addAttribute("totalSales", service.getTotalSales());
        m.addAttribute("totalPayments", service.getTotalPayments());
        m.addAttribute("totalDue", service.getTotalBalanceDue());
        m.addAttribute("totalDrBalance", service.getTotalDrBalance());
        m.addAttribute("totalCrBalance", service.getTotalCrBalance());

        return "clients/list";
    }

    @GetMapping({"/view/{code}", "/{code}"})
    public String view(@PathVariable String code, Model m) {
        Client client = service.findByIdWithSummary(code);
        List<SaleBill> sales = saleService.findByClientCode(code);
        List<PaymentReceived> payments = paymentService.findByClientCode(code);

        m.addAttribute("client", client);
        m.addAttribute("sales", sales);
        m.addAttribute("payments", payments);
        return "clients/view";
    }

    @GetMapping("/new")
    public String showForm(Model m) {
        m.addAttribute("client", new Client());
        return "clients/form";
    }

    @PostMapping
    public String save(@ModelAttribute Client c) {
        service.save(c);
        return "redirect:/clients";
    }

    @GetMapping("/edit/{code}")
    public String edit(@PathVariable String code, Model m) {
        m.addAttribute("client", service.findById(code));
        return "clients/form";
    }

    @PostMapping("/update/{code}")
    public String update(@PathVariable String code, @ModelAttribute Client c) {
        c.setClientCode(code);
        service.update(c);
        return "redirect:/clients";
    }

    @PostMapping("/delete/{code}")
    public String delete(@PathVariable String code) {
        try {
            service.delete(code);
            return "redirect:/clients?success=Client+" + code + "+deleted+successfully";
        } catch (Exception e) {
            return "redirect:/clients?error=Cannot+delete+client+" + code + ":+client+has+associated+bills+or+payments.";
        }
    }
}
