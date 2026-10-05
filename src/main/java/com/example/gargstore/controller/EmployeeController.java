package com.example.gargstore.controller;
import com.example.gargstore.service.EmployeeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping("/employees")
public class EmployeeController {
    @Autowired private EmployeeService empService;

    @GetMapping
    public String list(@RequestParam(defaultValue = "1") int page, Model m) {
        int pageSize = 25;
        int total = empService.count();
        int totalPages = Math.max(1, (int) Math.ceil((double) total / pageSize));
        if (page < 1) page = 1;
        if (page > totalPages && total > 0) page = totalPages;

        m.addAttribute("employees", empService.findPaged(page, pageSize));
        m.addAttribute("currentPage", page);
        m.addAttribute("totalPages", totalPages);
        m.addAttribute("totalRecords", total);
        m.addAttribute("pageSize", pageSize);
        return "employees/list";
    }
}
