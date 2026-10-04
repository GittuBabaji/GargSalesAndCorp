package com.example.gargstore.controller;
import com.example.gargstore.model.StockItem; import com.example.gargstore.service.StockItemService; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.*;
@Controller @RequestMapping("/inventory")
public class StockController {
    @Autowired private StockItemService service;
    @GetMapping public String list(Model m) { m.addAttribute("items", service.findAll()); return "inventory/list"; }
    @GetMapping("/new") public String showForm(Model m) { m.addAttribute("item", new StockItem()); return "inventory/form"; }
    @PostMapping public String save(@ModelAttribute StockItem s) { service.save(s); return "redirect:/inventory"; }
    @GetMapping("/edit/{code}") public String edit(@PathVariable String code, Model m) { m.addAttribute("item", service.findById(code)); return "inventory/form"; }
    @PostMapping("/update/{code}") public String update(@PathVariable String code, @ModelAttribute StockItem s) { s.setItemCode(code); service.update(s); return "redirect:/inventory"; }
    @PostMapping("/delete/{code}") public String delete(@PathVariable String code) { service.delete(code); return "redirect:/inventory"; }
}
