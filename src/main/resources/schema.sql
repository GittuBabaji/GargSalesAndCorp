-- GARG VARIETY STORE — Relational Schema (2NF-verified)

DROP DATABASE IF EXISTS garg_variety_store;
CREATE DATABASE garg_variety_store;
USE garg_variety_store;

-- 1. CLIENT
CREATE TABLE Client (
    Client_Code   VARCHAR(10) PRIMARY KEY,
    Name          VARCHAR(100) NOT NULL,
    Address       VARCHAR(255),
    Locality      VARCHAR(100),
    Phone_No      VARCHAR(15),
    GST_No        VARCHAR(20) UNIQUE,
    DR_Balance    DECIMAL(12,2) NOT NULL DEFAULT 0 CHECK (DR_Balance >= 0),
    CR_Balance    DECIMAL(12,2) NOT NULL DEFAULT 0 CHECK (CR_Balance >= 0)
);

-- 2. SUPPLIER
CREATE TABLE Supplier (
    Supplier_Code VARCHAR(10) PRIMARY KEY,
    Name          VARCHAR(100) NOT NULL,
    Address       VARCHAR(255),
    Locality      VARCHAR(100),
    Phone_No      VARCHAR(15),
    GST_No        VARCHAR(20) UNIQUE
);

-- 3. STOCK_ITEM
CREATE TABLE Stock_Item (
    Item_Code     VARCHAR(10) PRIMARY KEY,
    Item_Name     VARCHAR(100) NOT NULL,
    Category      VARCHAR(50),
    Unit          VARCHAR(15),
    Quantity      INT NOT NULL DEFAULT 0 CHECK (Quantity >= 0),
    Cost_Price    DECIMAL(10,2) NOT NULL CHECK (Cost_Price >= 0),
    Selling_Price DECIMAL(10,2) NOT NULL CHECK (Selling_Price >= 0),
    Reorder_Level INT NOT NULL DEFAULT 0 CHECK (Reorder_Level >= 0)
);

-- 4. FINANCIAL_SUMMARY
CREATE TABLE Financial_Summary (
    Period_Id         VARCHAR(10) PRIMARY KEY,
    Period            VARCHAR(30) NOT NULL,
    Total_Assets      DECIMAL(14,2) NOT NULL DEFAULT 0,
    Total_Liabilities DECIMAL(14,2) NOT NULL DEFAULT 0,
    Operating_Cost    DECIMAL(14,2) NOT NULL DEFAULT 0,
    Gross_Profit      DECIMAL(14,2) NOT NULL DEFAULT 0,
    Net_Profit        DECIMAL(14,2) NOT NULL DEFAULT 0,
    Tax               DECIMAL(14,2) NOT NULL DEFAULT 0
);

-- 5. EMPLOYEE

CREATE TABLE Employee (
    Employee_Code    VARCHAR(10) PRIMARY KEY,
    Name             VARCHAR(100) NOT NULL,
    Designation      VARCHAR(50),
    Phone_No         VARCHAR(15),
    Date_of_Joining  DATE,
    Salary           DECIMAL(10,2) NOT NULL CHECK (Salary >= 0)
);

-- 6. PURCHASE_BILL 
CREATE TABLE Purchase_Bill (
    Purchase_Bill_No VARCHAR(15) PRIMARY KEY,
    Bill_Date        DATE NOT NULL,
    Supplier_Code    VARCHAR(10) NOT NULL,
    Total_Amount     DECIMAL(12,2) NOT NULL CHECK (Total_Amount >= 0),
    Amount_Paid      DECIMAL(12,2) NOT NULL DEFAULT 0 CHECK (Amount_Paid >= 0),
    Balance_Due      DECIMAL(12,2) NOT NULL DEFAULT 0 CHECK (Balance_Due >= 0),
    Period_Id        VARCHAR(10),
    FOREIGN KEY (Supplier_Code) REFERENCES Supplier(Supplier_Code)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (Period_Id) REFERENCES Financial_Summary(Period_Id)
);

-- 7. SALE_BILL  
CREATE TABLE Sale_Bill (
    Bill_No       VARCHAR(15) PRIMARY KEY,
    Bill_Date     DATE NOT NULL,
    Client_Code   VARCHAR(10) NOT NULL,
    Total_Amount  DECIMAL(12,2) NOT NULL CHECK (Total_Amount >= 0),
    Payment_Mode  VARCHAR(15) CHECK (Payment_Mode IN ('Cash','Credit')),
    Balance_Due   DECIMAL(12,2) NOT NULL DEFAULT 0 CHECK (Balance_Due >= 0),
    Period_Id     VARCHAR(10),
    FOREIGN KEY (Client_Code) REFERENCES Client(Client_Code)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (Period_Id) REFERENCES Financial_Summary(Period_Id)
);

-- 8. PAYMENT_RECEIVED 
CREATE TABLE Payment_Received (
    Receipt_No       VARCHAR(15) PRIMARY KEY,
    Client_Code      VARCHAR(10) NOT NULL,
    Date_Received    DATE NOT NULL,
    Amount_Received  DECIMAL(12,2) NOT NULL CHECK (Amount_Received > 0),
    Payment_Mode     VARCHAR(15) CHECK (Payment_Mode IN ('Cash','Cheque','Online Transfer')),
    FOREIGN KEY (Client_Code) REFERENCES Client(Client_Code)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

-- 9. PURCHASE_BILL_ITEM 
CREATE TABLE Purchase_Bill_Item (
    Purchase_Bill_No VARCHAR(15) NOT NULL,
    Item_Code        VARCHAR(10) NOT NULL,
    Quantity         INT NOT NULL CHECK (Quantity > 0),
    Rate             DECIMAL(10,2) NOT NULL CHECK (Rate >= 0),
    Amount           DECIMAL(12,2) NOT NULL CHECK (Amount >= 0),
    PRIMARY KEY (Purchase_Bill_No, Item_Code),
    FOREIGN KEY (Purchase_Bill_No) REFERENCES Purchase_Bill(Purchase_Bill_No)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Item_Code) REFERENCES Stock_Item(Item_Code)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

-- 10. SALE_BILL_ITEM 
CREATE TABLE Sale_Bill_Item (
    Bill_No       VARCHAR(15) NOT NULL,
    Item_Code     VARCHAR(10) NOT NULL,
    Quantity_Sold INT NOT NULL CHECK (Quantity_Sold > 0),
    Rate_Applied  DECIMAL(10,2) NOT NULL CHECK (Rate_Applied >= 0),
    Amount        DECIMAL(12,2) NOT NULL CHECK (Amount >= 0),
    PRIMARY KEY (Bill_No, Item_Code),
    FOREIGN KEY (Bill_No) REFERENCES Sale_Bill(Bill_No)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Item_Code) REFERENCES Stock_Item(Item_Code)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

-- 11. EMPLOYEE_SALARY_RECORD 
CREATE TABLE Employee_Salary_Record (
    Employee_Code VARCHAR(10) NOT NULL,
    Period_Id     VARCHAR(10) NOT NULL,
    Salary_Paid   DECIMAL(10,2) NOT NULL CHECK (Salary_Paid >= 0),
    PRIMARY KEY (Employee_Code, Period_Id),
    FOREIGN KEY (Employee_Code) REFERENCES Employee(Employee_Code)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Period_Id) REFERENCES Financial_Summary(Period_Id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);
