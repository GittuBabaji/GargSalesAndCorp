package com.example.gargstore.controller;
import com.example.gargstore.service.EmployeeService; import org.springframework.beans.factory.annotation.Autowired; import org.springframework.stereotype.Controller; import org.springframework.ui.Model; import org.springframework.web.bind.annotation.GetMapping; import org.springframework.web.bind.annotation.RequestMapping;
@Controller @RequestMapping("/employees")
public class EmployeeController {
    @Autowired private EmployeeService empService;
    @GetMapping public String list(Model m) { m.addAttribute("employees", empService.findAll()); return "employees/list"; }
}
