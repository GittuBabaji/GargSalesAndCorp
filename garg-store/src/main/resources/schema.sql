CREATE TABLE IF NOT EXISTS Client (
    Client_Code VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(255),
    Locality VARCHAR(100),
    Phone_No VARCHAR(15),
    GST_No VARCHAR(20) UNIQUE,
    DR_Balance DECIMAL(12,2) DEFAULT 0 CHECK (DR_Balance >= 0),
    CR_Balance DECIMAL(12,2) DEFAULT 0 CHECK (CR_Balance >= 0)
);

CREATE TABLE IF NOT EXISTS Supplier (
    Supplier_Code VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(255),
    Locality VARCHAR(100),
    Phone_No VARCHAR(15),
    GST_No VARCHAR(20) UNIQUE
);

CREATE TABLE IF NOT EXISTS Stock_Item (
    Item_Code VARCHAR(10) PRIMARY KEY,
    Item_Name VARCHAR(100) NOT NULL,
    Category VARCHAR(50),
    Unit VARCHAR(15),
    Quantity INT NOT NULL DEFAULT 0 CHECK (Quantity >= 0),
    Cost_Price DECIMAL(10,2) NOT NULL CHECK (Cost_Price >= 0),
    Selling_Price DECIMAL(10,2) NOT NULL CHECK (Selling_Price >= 0),
    Reorder_Level INT NOT NULL DEFAULT 0 CHECK (Reorder_Level >= 0)
);

CREATE TABLE IF NOT EXISTS Financial_Summary (
    Period_Id VARCHAR(10) PRIMARY KEY,
    Period VARCHAR(30) NOT NULL,
    Total_Assets DECIMAL(14,2) DEFAULT 0,
    Total_Liabilities DECIMAL(14,2) DEFAULT 0,
    Operating_Cost DECIMAL(14,2) DEFAULT 0,
    Gross_Profit DECIMAL(14,2) DEFAULT 0,
    Net_Profit DECIMAL(14,2) DEFAULT 0,
    Tax DECIMAL(14,2) DEFAULT 0
);

CREATE TABLE IF NOT EXISTS Employee (
    Employee_Code VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Designation VARCHAR(50),
    Phone_No VARCHAR(15),
    Date_of_Joining DATE,
    Salary DECIMAL(10,2) NOT NULL,
    Period_Id VARCHAR(10),
    CONSTRAINT fk_emp_period FOREIGN KEY (Period_Id) REFERENCES Financial_Summary(Period_Id)
);

CREATE TABLE IF NOT EXISTS Purchase_Bill (
    Purchase_Bill_No VARCHAR(15) PRIMARY KEY,
    Bill_Date DATE NOT NULL,
    Supplier_Code VARCHAR(10) NOT NULL,
    Total_Amount DECIMAL(12,2) NOT NULL,
    Amount_Paid DECIMAL(12,2) NOT NULL DEFAULT 0,
    Balance_Due DECIMAL(12,2) NOT NULL DEFAULT 0,
    Period_Id VARCHAR(10),
    CONSTRAINT fk_pb_supplier FOREIGN KEY (Supplier_Code) REFERENCES Supplier(Supplier_Code) ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_pb_period FOREIGN KEY (Period_Id) REFERENCES Financial_Summary(Period_Id)
);

CREATE TABLE IF NOT EXISTS Sale_Bill (
    Bill_No VARCHAR(15) PRIMARY KEY,
    Bill_Date DATE NOT NULL,
    Client_Code VARCHAR(10) NOT NULL,
    Total_Amount DECIMAL(12,2) NOT NULL,
    Payment_Mode VARCHAR(15),
    Balance_Due DECIMAL(12,2) NOT NULL DEFAULT 0,
    Period_Id VARCHAR(10),
    CONSTRAINT fk_sb_client FOREIGN KEY (Client_Code) REFERENCES Client(Client_Code) ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_sb_period FOREIGN KEY (Period_Id) REFERENCES Financial_Summary(Period_Id)
);

CREATE TABLE IF NOT EXISTS Payment_Received (
    Receipt_No VARCHAR(15) PRIMARY KEY,
    Client_Code VARCHAR(10) NOT NULL,
    Date_Received DATE NOT NULL,
    Amount_Received DECIMAL(12,2) NOT NULL,
    Payment_Mode VARCHAR(15),
    CONSTRAINT fk_pr_client FOREIGN KEY (Client_Code) REFERENCES Client(Client_Code) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Purchase_Bill_Item (
    Purchase_Bill_No VARCHAR(15) NOT NULL,
    Item_Code VARCHAR(10) NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    Rate DECIMAL(10,2) NOT NULL CHECK (Rate >= 0),
    Amount DECIMAL(12,2) NOT NULL CHECK (Amount >= 0),
    PRIMARY KEY (Purchase_Bill_No, Item_Code),
    CONSTRAINT fk_pbi_pb FOREIGN KEY (Purchase_Bill_No) REFERENCES Purchase_Bill(Purchase_Bill_No) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_pbi_item FOREIGN KEY (Item_Code) REFERENCES Stock_Item(Item_Code) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Sale_Bill_Item (
    Bill_No VARCHAR(15) NOT NULL,
    Item_Code VARCHAR(10) NOT NULL,
    Quantity_Sold INT NOT NULL CHECK (Quantity_Sold > 0),
    Rate_Applied DECIMAL(10,2) NOT NULL CHECK (Rate_Applied >= 0),
    Amount DECIMAL(12,2) NOT NULL CHECK (Amount >= 0),
    PRIMARY KEY (Bill_No, Item_Code),
    CONSTRAINT fk_sbi_sb FOREIGN KEY (Bill_No) REFERENCES Sale_Bill(Bill_No) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_sbi_item FOREIGN KEY (Item_Code) REFERENCES Stock_Item(Item_Code) ON UPDATE CASCADE ON DELETE RESTRICT
);
