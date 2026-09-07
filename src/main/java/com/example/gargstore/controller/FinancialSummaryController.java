package com.example.gargstore.controller;
import com.example.gargstore.service.FinancialSummaryService; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.GetMapping; import org.springframework.web.bind.annotation.RequestMapping;
@Controller @RequestMapping("/financial")
public class FinancialSummaryController {
    @Autowired private FinancialSummaryService finService;
    @GetMapping public String list(Model m) { m.addAttribute("summaries", finService.findAll()); return "financial/list"; }
}
