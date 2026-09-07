import os
def w(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

base = 'C:/Users/Asus/OneDrive/Desktop/khatta/garg-store/'

w(base + 'pom.xml', '''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.1.2</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.example</groupId>
    <artifactId>gargstore</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>gargstore</name>
    <description>Garg Variety Store</description>
    <properties>
        <java.version>17</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-jdbc</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>com.mysql</groupId>
            <artifactId>mysql-connector-j</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
''')

w(base + 'src/main/resources/application.properties', '''
spring.datasource.url=jdbc:mysql://localhost:3306/garg_variety_store?createDatabaseIfNotExist=true&useSSL=false
spring.datasource.username=root
spring.datasource.password=root
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.sql.init.mode=always
spring.sql.init.schema-locations=classpath:schema.sql
spring.sql.init.data-locations=classpath:data.sql
''')

w(base + 'src/main/java/com/example/gargstore/GargVarietyStoreApplication.java', '''
package com.example.gargstore;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class GargVarietyStoreApplication {
    public static void main(String[] args) {
        SpringApplication.run(GargVarietyStoreApplication.class, args);
    }
}
''')

w(base + 'src/main/resources/schema.sql', '''
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

CREATE INDEX idx_sb_client ON Sale_Bill(Client_Code);
CREATE INDEX idx_sb_date ON Sale_Bill(Bill_Date);
CREATE INDEX idx_pb_supplier ON Purchase_Bill(Supplier_Code);
CREATE INDEX idx_pb_date ON Purchase_Bill(Bill_Date);
CREATE INDEX idx_pr_client ON Payment_Received(Client_Code);
CREATE INDEX idx_si_name ON Stock_Item(Item_Name);
CREATE INDEX idx_si_cat ON Stock_Item(Category);
''')

w(base + 'src/main/resources/data.sql', '''
INSERT IGNORE INTO Client (Client_Code, Name, Phone_No) VALUES ('C001', 'Test Client 1', '1234567890');
INSERT IGNORE INTO Supplier (Supplier_Code, Name, Phone_No) VALUES ('S001', 'Test Supplier 1', '0987654321');
INSERT IGNORE INTO Stock_Item (Item_Code, Item_Name, Quantity, Cost_Price, Selling_Price, Reorder_Level) VALUES ('I001', 'Test Item 1', 100, 10.0, 15.0, 10);
INSERT IGNORE INTO Financial_Summary (Period_Id, Period) VALUES ('P2023', 'FY 2023-24');
''')
