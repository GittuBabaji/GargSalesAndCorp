package com.example.gargstore.controller;
import com.example.gargstore.model.*; import com.example.gargstore.service.*; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.*; import java.util.ArrayList; import java.util.List;
@Controller @RequestMapping("/sales")
public class SaleBillController {
    @Autowired private SaleBillService saleService;
    @Autowired private ClientService clientService;
    @Autowired private StockItemService stockService;
    @Autowired private FinancialSummaryService finService;
    @GetMapping public String list(Model m) { m.addAttribute("sales", saleService.findAll()); return "sales/list"; }
    @GetMapping("/new") public String showForm(Model m) { m.addAttribute("sale", new SaleBill()); m.addAttribute("clients", clientService.findAll()); m.addAttribute("items", stockService.findAll()); m.addAttribute("summaries", finService.findAll()); return "sales/form"; }
    @PostMapping public String save(SaleBill sale, String[] itemCode, int[] quantitySold, double[] rateApplied, Model m) {
        if (sale.getPeriodId() != null && sale.getPeriodId().trim().isEmpty()) {
            sale.setPeriodId(null);
        }
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
}
