import random
from datetime import date, timedelta
from faker import Faker

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

OUT_FILE = "/mnt/c/Users/Asus/OneDrive/Desktop/khatta/garg-store/seed_data.sql"

N_CLIENTS = 100
N_SUPPLIERS = 10
N_ITEMS = 100
N_PERIODS = 24
N_EMPLOYEES = 5
N_PURCHASE_BILLS = 100
N_SALE_BILLS = 1000
N_PAYMENTS = 900

LOCALITIES = ["Sigra", "Lanka", "Assi", "Bhelupur", "Sunderpur", "Mahmoorganj",
              "Nadesar", "Cantt", "Godowlia", "Chetganj"]
DESIGNATIONS = ["Store Manager", "Cashier", "Sales Assistant", "Accountant", "Inventory Clerk"]

PRODUCTS = [
    ("Nestle Maggi 2-Minute Noodles 70g", "Noodles", "Pack"),
    ("Nestle Maggi Masala-ae-Magic 12g", "Condiments", "Pack"),
    ("Nescafe Classic Coffee 50g", "Beverages", "Pack"),
    ("Nescafe Sunrise Coffee 100g", "Beverages", "Pack"),
    ("Nestle KitKat 4-Finger", "Chocolates", "Pcs"),
    ("Nestle Munch", "Chocolates", "Pcs"),
    ("Nestle Milkybar", "Chocolates", "Pcs"),
    ("Nestle Milo Health Drink 400g", "Beverages", "Pack"),
    ("Nestle Milkmaid Condensed Milk 400g", "Dairy", "Pack"),
    ("Nestle Everyday Dairy Whitener 400g", "Dairy", "Pack"),
    ("Nestle A+ Toned Milk 500ml", "Dairy", "Pack"),
    ("Nestle Slim Milk 1L", "Dairy", "Pack"),
    ("Nestle Nesplak Chocolate Spread 290g", "Spreads", "Pack"),
    ("Nestle Cerelac Infant Cereal 300g", "Baby Food", "Pack"),
    ("Nestle Ceregrow Cereal 300g", "Baby Food", "Pack"),
    ("Parle-G Original Glucose Biscuits 200g", "Biscuits", "Pack"),
    ("Parle Monaco Salted Crackers 200g", "Biscuits", "Pack"),
    ("Parle Krackjack Sweet & Salty Biscuits 200g", "Biscuits", "Pack"),
    ("Parle Hide & Seek Chocolate Chip Cookies 120g", "Biscuits", "Pack"),
    ("Parle 20-20 Cashew Cookies 200g", "Biscuits", "Pack"),
    ("Parle Melody Toffee Pack", "Candy", "Pack"),
    ("Parle Poppins Candy Pack", "Candy", "Pack"),
    ("Parle Mango Bite Candy Pack", "Candy", "Pack"),
    ("Parle Kismi Toffee Bar", "Candy", "Pcs"),
    ("Parle Full Toss Toffee Pack", "Candy", "Pack"),
    ("Parle Rusk 200g", "Bakery", "Pack"),
    ("Parle Happy Happy Choco Chip Biscuits 100g", "Biscuits", "Pack"),
    ("Britannia Good Day Butter Cookies 200g", "Biscuits", "Pack"),
    ("Britannia Good Day Cashew Cookies 200g", "Biscuits", "Pack"),
    ("Britannia Marie Gold Biscuits 200g", "Biscuits", "Pack"),
    ("Britannia Bourbon Chocolate Cream Biscuits 150g", "Biscuits", "Pack"),
    ("Britannia Milk Bikis 200g", "Biscuits", "Pack"),
    ("Britannia NutriChoice Digestive 250g", "Biscuits", "Pack"),
    ("Britannia NutriChoice 5 Grain 250g", "Biscuits", "Pack"),
    ("Britannia Little Hearts 75g", "Biscuits", "Pack"),
    ("Britannia Tiger Krunch Chocolatey Biscuits 150g", "Biscuits", "Pack"),
    ("Britannia Cheese Slices 200g", "Dairy", "Pack"),
    ("Britannia Bread 400g", "Bakery", "Pack"),
    ("Britannia Rusk Toast 200g", "Bakery", "Pack"),
    ("Britannia Treat Jim Jam Biscuits 120g", "Biscuits", "Pack"),
    ("Lays Classic Salted Potato Chips 52g", "Snacks", "Pack"),
    ("Lays Magic Masala Potato Chips 52g", "Snacks", "Pack"),
    ("Lays India Magic Masala Chips 90g", "Snacks", "Pack"),
    ("Lays American Style Cream & Onion 52g", "Snacks", "Pack"),
    ("Lays Spanish Tomato Tango 52g", "Snacks", "Pack"),
    ("Lays Chile Limon Chips 52g", "Snacks", "Pack"),
    ("Lays Wafer Style Chips 90g", "Snacks", "Pack"),
    ("Lays Sizzlin Hot Chips 52g", "Snacks", "Pack"),
    ("Bingo Mad Angles Achaari Masti 90g", "Snacks", "Pack"),
    ("Bingo Tedhe Medhe Masala Madness 90g", "Snacks", "Pack"),
    ("Bingo Yumitos Potato Chips 52g", "Snacks", "Pack"),
    ("Bingo Original Style Potato Chips 90g", "Snacks", "Pack"),
    ("Bingo Treat Chocolate Wafers 100g", "Snacks", "Pack"),
    ("Bingo Zingg Chilli Sprinkled Chips 78g", "Snacks", "Pack"),
    ("Cadbury Dairy Milk Chocolate 55g", "Chocolates", "Pcs"),
    ("Cadbury Dairy Milk Silk 60g", "Chocolates", "Pcs"),
    ("Cadbury 5 Star Chocolate Bar", "Chocolates", "Pcs"),
    ("Cadbury Perk Chocolate Bar", "Chocolates", "Pcs"),
    ("Cadbury Bournvita Health Drink 500g", "Beverages", "Pack"),
    ("Cadbury Gems Chocolate Pack", "Chocolates", "Pack"),
    ("Amul Butter 100g", "Dairy", "Pack"),
    ("Amul Gold Full Cream Milk 500ml", "Dairy", "Pack"),
    ("Amul Cheese Slices 200g", "Dairy", "Pack"),
    ("Amul Taaza Toned Milk 500ml", "Dairy", "Pack"),
    ("Amul Ice Cream Cup 100ml", "Dairy", "Pcs"),
    ("Haldirams Aloo Bhujia 200g", "Snacks", "Pack"),
    ("Haldirams Moong Dal Namkeen 200g", "Snacks", "Pack"),
    ("Haldirams Soan Papdi 250g", "Sweets", "Pack"),
    ("Haldirams Bhel Puri 150g", "Snacks", "Pack"),
    ("Tata Salt 1kg", "Groceries", "Pack"),
    ("Tata Tea Gold 250g", "Beverages", "Pack"),
    ("Tata Sampann Toor Dal 1kg", "Groceries", "Pack"),
    ("Fortune Sunflower Oil 1L", "Groceries", "Pack"),
    ("Aashirvaad Atta 5kg", "Groceries", "Pack"),
    ("MDH Deggi Mirch Masala 100g", "Spices", "Pack"),
    ("Everest Garam Masala 100g", "Spices", "Pack"),
    ("Colgate MaxFresh Toothpaste 150g", "Personal Care", "Pack"),
    ("Colgate Strong Teeth Toothpaste 200g", "Personal Care", "Pack"),
    ("Closeup Red Hot Toothpaste 150g", "Personal Care", "Pack"),
    ("Dettol Handwash 200ml", "Personal Care", "Pack"),
    ("Lifebuoy Total Soap 125g", "Personal Care", "Pcs"),
    ("Lux Soft Touch Soap 100g", "Personal Care", "Pcs"),
    ("Dove Cream Beauty Bar Soap 100g", "Personal Care", "Pcs"),
    ("Head & Shoulders Shampoo 180ml", "Personal Care", "Pack"),
    ("Clinic Plus Shampoo 175ml", "Personal Care", "Pack"),
    ("Surf Excel Detergent Powder 1kg", "Household", "Pack"),
    ("Ariel Detergent Powder 1kg", "Household", "Pack"),
    ("Vim Dishwash Bar 200g", "Household", "Pcs"),
    ("Harpic Toilet Cleaner 500ml", "Household", "Pack"),
    ("Good Knight Mosquito Repellent Refill", "Household", "Pcs"),
    ("Odonil Air Freshener Block", "Household", "Pcs"),
    ("Kissan Mixed Fruit Jam 500g", "Spreads", "Pack"),
    ("Kissan Tomato Ketchup 500g", "Condiments", "Pack"),
    ("Maggi Hot & Sweet Tomato Chilli Sauce 500g", "Condiments", "Pack"),
    ("Real Fruit Juice Mixed Fruit 1L", "Beverages", "Pack"),
    ("Frooti Mango Drink 200ml", "Beverages", "Pcs"),
    ("Coca-Cola 750ml", "Beverages", "Pcs"),
    ("Sprite 750ml", "Beverages", "Pcs"),
    ("Thums Up 750ml", "Beverages", "Pcs"),
    ("Bisleri Mineral Water 1L", "Beverages", "Pcs"),
    ("Horlicks Health Drink 500g", "Beverages", "Pack"),
    ("Complan Nutrition Drink 500g", "Beverages", "Pack"),
    ("Patanjali Ghee 500ml", "Dairy", "Pack"),
    ("Patanjali Honey 250g", "Groceries", "Pack"),
    ("Pidilite Fevicol Adhesive 50g", "Stationery", "Pcs"),
    ("Camlin Wax Crayons 12 Shades", "Stationery", "Pack"),
    ("Classmate Notebook 172 Pages", "Stationery", "Pcs"),
    ("Reynolds 045 Ball Pen", "Stationery", "Pcs"),
]

sql_lines = []


def esc(s):
    return str(s).replace("'", "''")


def add_insert(table, columns, values):
    vals_sql = []
    for v in values:
        if v is None:
            vals_sql.append("NULL")
        elif isinstance(v, str):
            vals_sql.append(f"'{esc(v)}'")
        elif isinstance(v, date):
            vals_sql.append(f"'{v.isoformat()}'")
        else:
            vals_sql.append(str(v))
    sql_lines.append(
        f"INSERT IGNORE INTO {table} ({', '.join(columns)}) VALUES ({', '.join(vals_sql)});"
    )


# 1. CLIENT
client_codes = []
sql_lines.append("-- 1. CLIENT")
for i in range(1, N_CLIENTS + 1):
    code = f"CL{i:03d}"
    client_codes.append(code)
    dr = round(random.uniform(0, 25000), 2)
    cr = round(random.uniform(0, 5000), 2) if random.random() < 0.2 else 0.00
    add_insert(
        "Client",
        ["Client_Code", "Name", "Address", "Locality", "Phone_No", "GST_No", "DR_Balance", "CR_Balance"],
        [code, fake.company()[:100], fake.street_address()[:255], random.choice(LOCALITIES),
         f"9{random.randint(100000000, 999999999)}",
         f"09AAAAA{i:04d}A1Z{i%9+1}" if random.random() < 0.7 else None,
         dr, cr]
    )

# 2. SUPPLIER
supplier_codes = []
sql_lines.append("\n-- 2. SUPPLIER")
for i in range(1, N_SUPPLIERS + 1):
    code = f"SUP{i:03d}"
    supplier_codes.append(code)
    add_insert(
        "Supplier",
        ["Supplier_Code", "Name", "Address", "Locality", "Phone_No", "GST_No"],
        [code, fake.company()[:100] + " Traders", fake.street_address()[:255], random.choice(LOCALITIES),
         f"8{random.randint(100000000, 999999999)}",
         f"07BBBBB{i:04d}B1Z{i%9+1}"]
    )

# 3. STOCK_ITEM
item_codes = []
items_info = {}
sql_lines.append("\n-- 3. STOCK_ITEM")

product_pool = PRODUCTS.copy()
random.shuffle(product_pool)
chosen_products = []
extra_sizes = ["Family Pack", "Value Pack", "Small Pack", "Combo Pack"]
idx = 0
while len(chosen_products) < N_ITEMS:
    base_name, cat, unit = product_pool[idx % len(product_pool)]
    if idx < len(product_pool):
        chosen_products.append((base_name, cat, unit))
    else:
        variant = extra_sizes[(idx // len(product_pool) - 1) % len(extra_sizes)]
        chosen_products.append((f"{base_name} ({variant})", cat, unit))
    idx += 1

for i, (name, cat, unit) in enumerate(chosen_products, start=1):
    code = f"IT{i:03d}"
    item_codes.append(code)
    cost = round(random.uniform(8, 450), 2)
    sell = round(cost * random.uniform(1.1, 1.35), 2)
    qty = random.randint(0, 500)
    reorder = random.randint(5, 50)
    items_info[code] = (cost, sell)
    add_insert(
        "Stock_Item",
        ["Item_Code", "Item_Name", "Category", "Unit", "Quantity", "Cost_Price", "Selling_Price", "Reorder_Level"],
        [code, name, cat, unit, qty, cost, sell, reorder]
    )

# 4. FINANCIAL_SUMMARY
period_ids = []
period_dates = {}
sql_lines.append("\n-- 4. FINANCIAL_SUMMARY")
start_year, start_month = 2021, 1
for i in range(1, N_PERIODS + 1):
    pid = f"FY{i:03d}"
    month = (start_month + i - 1 - 1) % 12 + 1
    year = start_year + (start_month + i - 1 - 1) // 12
    label = date(year, month, 1).strftime("%b-%Y")
    period_ids.append(pid)
    period_dates[pid] = date(year, month, 1)
    assets = round(random.uniform(200000, 800000), 2)
    liabilities = round(random.uniform(50000, 300000), 2)
    op_cost = round(random.uniform(20000, 90000), 2)
    gross_profit = round(random.uniform(30000, 150000), 2)
    net_profit = round(gross_profit - op_cost, 2)
    tax = round(max(net_profit, 0) * 0.18, 2)
    add_insert(
        "Financial_Summary",
        ["Period_Id", "Period", "Total_Assets", "Total_Liabilities", "Operating_Cost",
         "Gross_Profit", "Net_Profit", "Tax"],
        [pid, label, assets, liabilities, op_cost, gross_profit, net_profit, tax]
    )

# 5. EMPLOYEE (no Period_Id — that goes in Employee_Salary_Record)
employee_codes = []
sql_lines.append("\n-- 5. EMPLOYEE")
for i in range(1, N_EMPLOYEES + 1):
    code = f"EMP{i:03d}"
    employee_codes.append(code)
    join_date = fake.date_between(start_date=date(2019, 1, 1), end_date=date(2025, 12, 31))
    salary = round(random.uniform(9000, 35000), 2)
    add_insert(
        "Employee",
        ["Employee_Code", "Name", "Designation", "Phone_No", "Date_of_Joining", "Salary"],
        [code, fake.name(), random.choice(DESIGNATIONS), f"7{random.randint(100000000, 999999999)}",
         join_date, salary]
    )

# 6. PURCHASE_BILL (totals computed after items)
purchase_bills = []
for i in range(1, N_PURCHASE_BILLS + 1):
    pb_no = f"PB{i:04d}"
    period_id = random.choice(period_ids)
    bill_date = period_dates[period_id] + timedelta(days=random.randint(0, 27))
    purchase_bills.append({
        "no": pb_no, "date": bill_date,
        "supplier": random.choice(supplier_codes), "period": period_id,
    })

# 9. PURCHASE_BILL_ITEM (generate first to total the parent bill)
purchase_bill_item_lines = []
for pb in purchase_bills:
    n_lines = random.randint(1, 5)
    chosen_items = random.sample(item_codes, n_lines)
    total = 0.0
    for item_code in chosen_items:
        cost_price, _ = items_info[item_code]
        qty = random.randint(1, 40)
        rate = round(cost_price * random.uniform(0.95, 1.05), 2)
        amount = round(qty * rate, 2)
        total += amount
        purchase_bill_item_lines.append((pb["no"], item_code, qty, rate, amount))
    pb["total"] = round(total, 2)
    pb["paid"] = round(pb["total"] * random.choice([1.0, 1.0, 0.5, 0.0, 0.75]), 2)
    pb["balance"] = round(pb["total"] - pb["paid"], 2)

sql_lines.append("\n-- 6. PURCHASE_BILL")
for pb in purchase_bills:
    add_insert(
        "Purchase_Bill",
        ["Purchase_Bill_No", "Bill_Date", "Supplier_Code", "Total_Amount", "Amount_Paid", "Balance_Due", "Period_Id"],
        [pb["no"], pb["date"], pb["supplier"], pb["total"], pb["paid"], pb["balance"], pb["period"]]
    )

# 7. SALE_BILL (same two-pass approach)
sale_bills = []
for i in range(1, N_SALE_BILLS + 1):
    b_no = f"SB{i:04d}"
    period_id = random.choice(period_ids)
    bill_date = period_dates[period_id] + timedelta(days=random.randint(0, 27))
    payment_mode = random.choice(["Cash", "Credit"])
    sale_bills.append({
        "no": b_no, "date": bill_date,
        "client": random.choice(client_codes), "period": period_id, "mode": payment_mode,
    })

sale_bill_item_lines = []
for sb in sale_bills:
    n_lines = random.randint(1, 5)
    chosen_items = random.sample(item_codes, n_lines)
    total = 0.0
    for item_code in chosen_items:
        _, sell_price = items_info[item_code]
        qty = random.randint(1, 20)
        rate = round(sell_price * random.uniform(0.97, 1.03), 2)
        amount = round(qty * rate, 2)
        total += amount
        sale_bill_item_lines.append((sb["no"], item_code, qty, rate, amount))
    sb["total"] = round(total, 2)
    if sb["mode"] == "Cash":
        sb["balance"] = 0.00
    else:
        sb["balance"] = round(sb["total"] * random.choice([0.0, 0.25, 0.5, 1.0]), 2)

sql_lines.append("\n-- 7. SALE_BILL")
for sb in sale_bills:
    add_insert(
        "Sale_Bill",
        ["Bill_No", "Bill_Date", "Client_Code", "Total_Amount", "Payment_Mode", "Balance_Due", "Period_Id"],
        [sb["no"], sb["date"], sb["client"], sb["total"], sb["mode"], sb["balance"], sb["period"]]
    )

# 8. PAYMENT_RECEIVED
sql_lines.append("\n-- 8. PAYMENT_RECEIVED")
for i in range(1, N_PAYMENTS + 1):
    r_no = f"RC{i:04d}"
    client = random.choice(client_codes)
    d_recv = fake.date_between(start_date=date(2021, 1, 1), end_date=date(2025, 12, 31))
    amount = round(random.uniform(500, 20000), 2)
    mode = random.choice(["Cash", "Cheque", "Online Transfer"])
    add_insert(
        "Payment_Received",
        ["Receipt_No", "Client_Code", "Date_Received", "Amount_Received", "Payment_Mode"],
        [r_no, client, d_recv, amount, mode]
    )

# 9. PURCHASE_BILL_ITEM
sql_lines.append("\n-- 9. PURCHASE_BILL_ITEM")
for pb_no, item_code, qty, rate, amount in purchase_bill_item_lines:
    add_insert(
        "Purchase_Bill_Item",
        ["Purchase_Bill_No", "Item_Code", "Quantity", "Rate", "Amount"],
        [pb_no, item_code, qty, rate, amount]
    )

# 10. SALE_BILL_ITEM
sql_lines.append("\n-- 10. SALE_BILL_ITEM")
for b_no, item_code, qty, rate, amount in sale_bill_item_lines:
    add_insert(
        "Sale_Bill_Item",
        ["Bill_No", "Item_Code", "Quantity_Sold", "Rate_Applied", "Amount"],
        [b_no, item_code, qty, rate, amount]
    )

# 11. EMPLOYEE_SALARY_RECORD
sql_lines.append("\n-- 11. EMPLOYEE_SALARY_RECORD")
for emp_code in employee_codes:
    for pid in period_ids:
        salary_paid = round(random.uniform(9000, 35000), 2)
        add_insert(
            "Employee_Salary_Record",
            ["Employee_Code", "Period_Id", "Salary_Paid"],
            [emp_code, pid, salary_paid]
        )

# Write file
with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write("-- =========================================================\n")
    f.write("-- GARG VARIETY STORE — Seed Data (auto-generated)\n")
    f.write("-- Run schema.sql first, then this file.\n")
    f.write("-- =========================================================\n\n")
    f.write("USE garg_variety_store;\n\n")
    f.write("SET FOREIGN_KEY_CHECKS = 0;\n")
    f.write("\n".join(sql_lines))
    f.write("\nSET FOREIGN_KEY_CHECKS = 1;\n")

print(f"Wrote {len(sql_lines)} lines to {OUT_FILE}")
