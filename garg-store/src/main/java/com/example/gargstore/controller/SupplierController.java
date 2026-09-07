package com.example.gargstore.controller;
import com.example.gargstore.model.Supplier; import com.example.gargstore.service.SupplierService; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.*;
@Controller @RequestMapping("/suppliers")
public class SupplierController {
    @Autowired private SupplierService service;
    @GetMapping public String list(Model m) { m.addAttribute("suppliers", service.findAll()); return "suppliers/list"; }
    @GetMapping("/new") public String showForm(Model m) { m.addAttribute("supplier", new Supplier()); return "suppliers/form"; }
    @PostMapping public String save(@ModelAttribute Supplier s) { service.save(s); return "redirect:/suppliers"; }
    @GetMapping("/edit/{code}") public String edit(@PathVariable String code, Model m) { m.addAttribute("supplier", service.findById(code)); return "suppliers/form"; }
    @PostMapping("/update/{code}") public String update(@PathVariable String code, @ModelAttribute Supplier s) { s.setSupplierCode(code); service.update(s); return "redirect:/suppliers"; }
    @PostMapping("/delete/{code}") public String delete(@PathVariable String code) { service.delete(code); return "redirect:/suppliers"; }
}
