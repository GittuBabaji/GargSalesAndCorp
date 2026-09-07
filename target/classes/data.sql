-- Financial Summaries
INSERT IGNORE INTO Financial_Summary (Period_Id, Period) VALUES ('P2023', 'FY 2023-24');
INSERT IGNORE INTO Financial_Summary (Period_Id, Period) VALUES ('P2024', 'FY 2024-25');

-- Clients
INSERT IGNORE INTO Client (Client_Code, Name, Phone_No, Address, Locality, DR_Balance, CR_Balance) VALUES ('C001', 'Ramesh Kumar', '9876543210', '12 MG Road', 'Central', 0, 0);
INSERT IGNORE INTO Client (Client_Code, Name, Phone_No, Address, Locality, DR_Balance, CR_Balance) VALUES ('C002', 'Suresh Gupta', '9876543211', '45 Park Street', 'North', 1500.00, 0);
INSERT IGNORE INTO Client (Client_Code, Name, Phone_No, Address, Locality, DR_Balance, CR_Balance) VALUES ('C003', 'Anita Sharma', '9876543212', '78 Lake View', 'South', 0, 500.00);
INSERT IGNORE INTO Client (Client_Code, Name, Phone_No, Address, Locality, DR_Balance, CR_Balance) VALUES ('C004', 'Kiran Patel', '9876543213', '101 Gandhi Nagar', 'West', 0, 0);
INSERT IGNORE INTO Client (Client_Code, Name, Phone_No, Address, Locality, DR_Balance, CR_Balance) VALUES ('C005', 'Vikram Singh', '9876543214', '222 Civil Lines', 'East', 8000.00, 0);

-- Suppliers
INSERT IGNORE INTO Supplier (Supplier_Code, Name, Phone_No, Address, Locality) VALUES ('S001', 'ABC Distributors', '9988776655', 'Plot 10, Industrial Area', 'North');
INSERT IGNORE INTO Supplier (Supplier_Code, Name, Phone_No, Address, Locality) VALUES ('S002', 'XYZ Wholesalers', '9988776656', 'Shed 5, Market Yard', 'South');
INSERT IGNORE INTO Supplier (Supplier_Code, Name, Phone_No, Address, Locality) VALUES ('S003', 'Mega Mart Supplies', '9988776657', 'Block C, Trade Center', 'Central');

-- Stock Items
INSERT IGNORE INTO Stock_Item (Item_Code, Item_Name, Category, Unit, Quantity, Cost_Price, Selling_Price, Reorder_Level) VALUES ('I001', 'Basmati Rice', 'Groceries', 'kg', 500, 80.00, 110.00, 50);
INSERT IGNORE INTO Stock_Item (Item_Code, Item_Name, Category, Unit, Quantity, Cost_Price, Selling_Price, Reorder_Level) VALUES ('I002', 'Toor Dal', 'Groceries', 'kg', 200, 120.00, 150.00, 30);
INSERT IGNORE INTO Stock_Item (Item_Code, Item_Name, Category, Unit, Quantity, Cost_Price, Selling_Price, Reorder_Level) VALUES ('I003', 'Sunflower Oil', 'Groceries', 'liter', 150, 130.00, 165.00, 20);
INSERT IGNORE INTO Stock_Item (Item_Code, Item_Name, Category, Unit, Quantity, Cost_Price, Selling_Price, Reorder_Level) VALUES ('I004', 'Bathing Soap', 'Toiletries', 'pcs', 800, 25.00, 35.00, 100);
INSERT IGNORE INTO Stock_Item (Item_Code, Item_Name, Category, Unit, Quantity, Cost_Price, Selling_Price, Reorder_Level) VALUES ('I005', 'Toothpaste', 'Toiletries', 'pcs', 300, 45.00, 60.00, 50);
INSERT IGNORE INTO Stock_Item (Item_Code, Item_Name, Category, Unit, Quantity, Cost_Price, Selling_Price, Reorder_Level) VALUES ('I006', 'Notebooks', 'Stationery', 'pcs', 1000, 30.00, 50.00, 200);
INSERT IGNORE INTO Stock_Item (Item_Code, Item_Name, Category, Unit, Quantity, Cost_Price, Selling_Price, Reorder_Level) VALUES ('I007', 'Ball Pens', 'Stationery', 'pcs', 10, 5.00, 10.00, 50); -- Deliberately low stock to test warning

-- Employees
INSERT IGNORE INTO Employee (Employee_Code, Name, Designation, Phone_No, Date_of_Joining, Salary, Period_Id) VALUES ('E001', 'Rahul Verma', 'Manager', '9001122334', '2023-01-15', 35000.00, 'P2023');
INSERT IGNORE INTO Employee (Employee_Code, Name, Designation, Phone_No, Date_of_Joining, Salary, Period_Id) VALUES ('E002', 'Priya Das', 'Cashier', '9001122335', '2023-03-01', 20000.00, 'P2023');
INSERT IGNORE INTO Employee (Employee_Code, Name, Designation, Phone_No, Date_of_Joining, Salary, Period_Id) VALUES ('E003', 'Amit Kumar', 'Store Keeper', '9001122336', '2023-05-10', 18000.00, 'P2023');
