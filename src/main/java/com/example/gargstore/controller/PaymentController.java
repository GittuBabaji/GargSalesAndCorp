package com.example.gargstore.controller;
import com.example.gargstore.model.PaymentReceived; import com.example.gargstore.service.PaymentReceivedService; import com.example.gargstore.service.ClientService; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.*;
@Controller @RequestMapping("/payments")
public class PaymentController {
    @Autowired private PaymentReceivedService payService;
    @Autowired private ClientService clientService;
    @GetMapping public String list(Model m) { m.addAttribute("payments", payService.findAll()); return "payments/list"; }
    @GetMapping("/new") public String showForm(Model m) { m.addAttribute("payment", new PaymentReceived()); m.addAttribute("clients", clientService.findAll()); return "payments/form"; }
    @PostMapping public String save(PaymentReceived p) { payService.receivePayment(p); return "redirect:/payments"; }
}
