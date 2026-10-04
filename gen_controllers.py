import os
def w(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
ct = 'C:/Users/Asus/OneDrive/Desktop/khatta/garg-store/src/main/java/com/example/gargstore/controller/'

w(ct+'DashboardController.java', '''package com.example.gargstore.controller;
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
}''')

w(ct+'ClientController.java', '''package com.example.gargstore.controller;
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
}''')

w(ct+'SupplierController.java', '''package com.example.gargstore.controller;
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
}''')

w(ct+'StockController.java', '''package com.example.gargstore.controller;
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
}''')

w(ct+'SaleBillController.java', '''package com.example.gargstore.controller;
import com.example.gargstore.model.*; import com.example.gargstore.service.*; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.*; import java.util.ArrayList; import java.util.List;
@Controller @RequestMapping("/sales")
public class SaleBillController {
    @Autowired private SaleBillService saleService;
    @Autowired private ClientService clientService;
    @Autowired private StockItemService stockService;
    @GetMapping public String list(Model m) { m.addAttribute("sales", saleService.findAll()); return "sales/list"; }
    @GetMapping("/new") public String showForm(Model m) { m.addAttribute("sale", new SaleBill()); m.addAttribute("clients", clientService.findAll()); m.addAttribute("items", stockService.findAll()); return "sales/form"; }
    @PostMapping public String save(SaleBill sale, String[] itemCode, int[] quantitySold, double[] rateApplied, Model m) {
        try {
            List<SaleBillItem> items = new ArrayList<>();
            for(int i=0; i<itemCode.length; i++){
                if(itemCode[i] != null && !itemCode[i].isEmpty()){
                    SaleBillItem it = new SaleBillItem(); it.setItemCode(itemCode[i]); it.setQuantitySold(quantitySold[i]); it.setRateApplied(rateApplied[i]); it.setAmount(quantitySold[i]*rateApplied[i]); items.add(it);
                }
            }
            saleService.createSale(sale, items);
            return "redirect:/sales";
        } catch(Exception e) { m.addAttribute("error", e.getMessage()); return "error"; }
    }
    @GetMapping("/{billNo}") public String view(@PathVariable String billNo, Model m) { m.addAttribute("sale", saleService.findById(billNo)); return "sales/view"; }
}''')

w(ct+'PurchaseBillController.java', '''package com.example.gargstore.controller;
import com.example.gargstore.model.*; import com.example.gargstore.service.*; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.*; import java.util.ArrayList; import java.util.List;
@Controller @RequestMapping("/purchases")
public class PurchaseBillController {
    @Autowired private PurchaseBillService purService;
    @Autowired private SupplierService supService;
    @Autowired private StockItemService stockService;
    @GetMapping public String list(Model m) { m.addAttribute("purchases", purService.findAll()); return "purchases/list"; }
    @GetMapping("/new") public String showForm(Model m) { m.addAttribute("purchase", new PurchaseBill()); m.addAttribute("suppliers", supService.findAll()); m.addAttribute("items", stockService.findAll()); return "purchases/form"; }
    @PostMapping public String save(PurchaseBill purchase, String[] itemCode, int[] quantity, double[] rate) {
        List<PurchaseBillItem> items = new ArrayList<>();
        for(int i=0; i<itemCode.length; i++){
            if(itemCode[i] != null && !itemCode[i].isEmpty()){
                PurchaseBillItem it = new PurchaseBillItem(); it.setItemCode(itemCode[i]); it.setQuantity(quantity[i]); it.setRate(rate[i]); it.setAmount(quantity[i]*rate[i]); items.add(it);
            }
        }
        purService.createPurchase(purchase, items); return "redirect:/purchases";
    }
    @GetMapping("/{billNo}") public String view(@PathVariable String billNo, Model m) { m.addAttribute("purchase", purService.findById(billNo)); return "purchases/view"; }
}''')

w(ct+'PaymentController.java', '''package com.example.gargstore.controller;
import com.example.gargstore.model.PaymentReceived; import com.example.gargstore.service.PaymentReceivedService; import com.example.gargstore.service.ClientService; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.*;
@Controller @RequestMapping("/payments")
public class PaymentController {
    @Autowired private PaymentReceivedService payService;
    @Autowired private ClientService clientService;
    @GetMapping public String list(Model m) { m.addAttribute("payments", payService.findAll()); return "payments/list"; }
    @GetMapping("/new") public String showForm(Model m) { m.addAttribute("payment", new PaymentReceived()); m.addAttribute("clients", clientService.findAll()); return "payments/form"; }
    @PostMapping public String save(PaymentReceived p) { payService.receivePayment(p); return "redirect:/payments"; }
}''')

w(ct+'ReportController.java', '''package com.example.gargstore.controller;
import org.springframework.stereotype.Controller; import org.springframework.web.bind.annotation.GetMapping;
@Controller
public class ReportController {
    @GetMapping("/reports") public String reports() { return "reports/index"; }
}''')

w(ct+'EmployeeController.java', '''package com.example.gargstore.controller;
import com.example.gargstore.service.EmployeeService; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.GetMapping; import org.springframework.web.bind.annotation.RequestMapping;
@Controller @RequestMapping("/employees")
public class EmployeeController {
    @Autowired private EmployeeService empService;
    @GetMapping public String list(Model m) { m.addAttribute("employees", empService.findAll()); return "employees/list"; }
}''')

w(ct+'FinancialSummaryController.java', '''package com.example.gargstore.controller;
import com.example.gargstore.service.FinancialSummaryService; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.GetMapping; import org.springframework.web.bind.annotation.RequestMapping;
@Controller @RequestMapping("/financial")
public class FinancialSummaryController {
    @Autowired private FinancialSummaryService finService;
    @GetMapping public String list(Model m) { m.addAttribute("summaries", finService.findAll()); return "financial/list"; }
}''')
