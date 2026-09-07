package com.example.gargstore.controller;
import com.example.gargstore.model.Client; import com.example.gargstore.service.ClientService; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.*;
@Controller @RequestMapping("/clients")
public class ClientController {
    @Autowired private ClientService service;
    @GetMapping public String list(Model m) { m.addAttribute("clients", service.findAll()); return "clients/list"; }
    @GetMapping("/new") public String showForm(Model m) { m.addAttribute("client", new Client()); return "clients/form"; }
    @PostMapping public String save(@ModelAttribute Client c) { service.save(c); return "redirect:/clients"; }
    @GetMapping("/edit/{code}") public String edit(@PathVariable String code, Model m) { m.addAttribute("client", service.findById(code)); return "clients/form"; }
    @PostMapping("/update/{code}") public String update(@PathVariable String code, @ModelAttribute Client c) { c.setClientCode(code); service.update(c); return "redirect:/clients"; }
    @PostMapping("/delete/{code}") public String delete(@PathVariable String code) { service.delete(code); return "redirect:/clients"; }
}
