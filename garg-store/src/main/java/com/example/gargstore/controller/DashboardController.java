package com.example.gargstore.controller;
import com.example.gargstore.service.*; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.GetMapping;
@Controller
public class DashboardController {
    @Autowired private ClientService clientService;
    @Autowired private SupplierService supplierService;
    @Autowired private StockItemService stockService;
    @Autowired private EmployeeService empService;
    @Autowired private com.example.gargstore.repository.SaleBillRepository saleRepo;
    @Autowired private com.example.gargstore.repository.PurchaseBillRepository purRepo;
    
    @GetMapping("/")
    public String dashboard(Model model) {
        model.addAttribute("totalClients", clientService.count());
        model.addAttribute("totalSuppliers", supplierService.count());
        model.addAttribute("totalItems", stockService.count());
        model.addAttribute("totalEmployees", empService.count());
        model.addAttribute("totalSales", saleRepo.getTotalSales());
        model.addAttribute("totalPurchases", purRepo.getTotalPurchases());
        model.addAttribute("lowStockItems", stockService.findLowStock());
        return "dashboard";
    }
}
