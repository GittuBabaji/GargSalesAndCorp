# Garg Variety Store - Billing and Inventory Management System

## 1. Project Overview
A complete web application for managing retail store billing and inventory, built using Spring Boot, JdbcTemplate, Thymeleaf, and MySQL.

## 2. Client Requirements
- Manage Clients, Suppliers, Stock Items, Bills, Payments, Employees, and Financial Summaries.
- No JPA, Hibernate, React, Angular, Vue, Lombok.
- Strictly adhere to the supplied ER schema.
- Uses transactions.

## 3. Technology Stack
- **Backend:** Java 17, Spring Boot 3
- **Database:** MySQL
- **DB Access:** Spring JDBC (JdbcTemplate)
- **UI:** Thymeleaf, HTML, CSS, Vanilla JS
- **Build:** Maven

## 4. ER Diagram Explanation
The ER model represents a retail store with 10 tables handling sales, purchases, inventory, payments, and financials. Entities are properly linked via foreign keys maintaining referential integrity.

## 5-11. Database Schema
- **Client**: Stores customer info. PK: Client_Code.
- **Supplier**: Stores supplier info. PK: Supplier_Code.
- **Stock_Item**: Inventory tracker. PK: Item_Code.
- **Financial_Summary**: Accounting periods. PK: Period_Id.
- **Employee**: Staff details linked to period.
- **Purchase_Bill** & **Sale_Bill**: Headers for transactions.
- **Purchase_Bill_Item** & **Sale_Bill_Item**: Line items for M:N relations between bills and items.
- **Payment_Received**: Tracks payments from clients.

## 12. JdbcTemplate Explanation
Spring's JdbcTemplate is used for all database operations instead of JPA. It maps result sets to Java models directly.

## 13. Thymeleaf Explanation
Thymeleaf handles server-side rendering for the web pages, passing model attributes directly to HTML templates using tags like 	h:each and 	h:text.

## 14. Spring Boot Architecture
- **Controller:** Maps web requests to endpoints, coordinates with Services, prepares Models for Views.
- **Service:** Contains business logic and transaction boundaries.
- **Repository:** Interacts directly with MySQL via JdbcTemplate.

## 15. Transaction Handling
@Transactional is applied in SaleBillService, PurchaseBillService, and PaymentReceivedService. Operations on items, bills, stock counts, and balances are committed wholly or rolled back completely upon any exception.

## 16. Indexing
- idx_sb_client: For fast querying of sales by client.
- idx_sb_date: For reporting on date ranges.
- idx_pb_supplier: For purchasing reports.
- idx_pb_date: Purchase tracking.
- idx_pr_client: Fast payment lookup.
- idx_si_name & idx_si_cat: Inventory searching.

## 17. SQL Queries
Uses SELECT, INSERT, UPDATE, DELETE, and aggregations (SUM) parameterized safely.

## 18-21. Configuration & Running
1. Configure MySQL credentials in src/main/resources/application.properties.
2. Run mvn clean package to build.
3. Start the application: java -jar target/gargstore-0.0.1-SNAPSHOT.jar
4. Available URLs: /, /clients, /suppliers, /inventory, /sales, /purchases, /payments, /employees, /financial, /reports.

No authentication is added, adhering directly to requirements.
