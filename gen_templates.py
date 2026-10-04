import os
def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
tm = 'C:/Users/Asus/OneDrive/Desktop/khatta/garg-store/src/main/resources/templates/'

w(tm+'layout.html', '''<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:fragment="head(title)">
    <title th:text="">App</title>
    <style>
        body { font-family: Arial, sans-serif; margin:0; display:flex; background-color:#f4f4f4;}
        .sidebar { width: 250px; background: #333; color: #fff; min-height: 100vh; padding: 20px;}
        .sidebar a { color: #fff; text-decoration: none; display: block; padding: 10px 0;}
        .content { flex: 1; padding: 20px;}
        table { width:100%; border-collapse:collapse; background: #fff; margin-bottom:20px;}
        th, td { border: 1px solid #ddd; padding: 8px;}
        th { background: #eee;}
        .btn { padding: 5px 10px; background: #007bff; color: #fff; text-decoration:none; border:none; cursor:pointer;}
        .alert { color: red; }
    </style>
</head>
<body>
    <div th:fragment="sidebar" class="sidebar">
        <h2>Garg Variety Store</h2>
        <a href="/">Dashboard</a>
        <a href="/sales">Sales</a>
        <a href="/purchases">Purchases</a>
        <a href="/inventory">Inventory</a>
        <a href="/clients">Clients</a>
        <a href="/suppliers">Suppliers</a>
        <a href="/payments">Payments</a>
        <a href="/employees">Employees</a>
        <a href="/financial">Financial Summary</a>
        <a href="/reports">Reports</a>
    </div>
</body>
</html>''')

w(tm+'dashboard.html', '''<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{layout :: head('Dashboard')}"></head>
<body>
    <div th:replace="~{layout :: sidebar}"></div>
    <div class="content">
        <h1>Dashboard</h1>
        <div style="display:flex; gap:20px;">
            <div style="background:#fff; padding:20px; border:1px solid #ddd;">Total Clients: <span th:text=""></span></div>
            <div style="background:#fff; padding:20px; border:1px solid #ddd;">Total Suppliers: <span th:text=""></span></div>
            <div style="background:#fff; padding:20px; border:1px solid #ddd;">Total Sales: <span th:text=""></span></div>
            <div style="background:#fff; padding:20px; border:1px solid #ddd;">Total Purchases: <span th:text=""></span></div>
        </div>
        <h2>Low Stock Alerts</h2>
        <table>
            <tr><th>Code</th><th>Name</th><th>Quantity</th><th>Reorder Level</th></tr>
            <tr th:each="i : ">
                <td th:text=""></td><td th:text=""></td>
                <td th:text="" style="color:red; font-weight:bold;"></td><td th:text=""></td>
            </tr>
        </table>
    </div>
</body>
</html>''')

w(tm+'clients/list.html', '''<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{layout :: head('Clients')}"></head>
<body>
    <div th:replace="~{layout :: sidebar}"></div>
    <div class="content">
        <h1>Clients <a href="/clients/new" class="btn">+ Add New</a></h1>
        <table>
            <tr><th>Code</th><th>Name</th><th>Phone</th><th>DR Balance</th><th>CR Balance</th><th>Actions</th></tr>
            <tr th:each="c : ">
                <td th:text=""></td><td th:text=""></td><td th:text=""></td>
                <td th:text=""></td><td th:text=""></td>
                <td>
                    <a th:href="@{/clients/edit/{id}(id=)}" class="btn">Edit</a>
                    <form th:action="@{/clients/delete/{id}(id=)}" method="post" style="display:inline;"><button type="submit" class="btn" style="background:red;">Del</button></form>
                </td>
            </tr>
        </table>
    </div>
</body>
</html>''')

w(tm+'clients/form.html', '''<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{layout :: head('Client Form')}"></head>
<body>
    <div th:replace="~{layout :: sidebar}"></div>
    <div class="content">
        <h1 th:text=""></h1>
        <form th:action="" method="post">
            <div th:if="">Code: <input type="text" name="clientCode" required/></div>
            <div>Name: <input type="text" name="name" th:value="" required/></div>
            <div>Phone: <input type="text" name="phoneNo" th:value=""/></div>
            <button type="submit" class="btn">Save</button>
        </form>
    </div>
</body>
</html>''')

w(tm+'inventory/list.html', '''<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{layout :: head('Inventory')}"></head>
<body>
    <div th:replace="~{layout :: sidebar}"></div>
    <div class="content">
        <h1>Inventory <a href="/inventory/new" class="btn">+ Add Item</a></h1>
        <table>
            <tr><th>Code</th><th>Name</th><th>Qty</th><th>Price</th><th>Reorder</th><th>Actions</th></tr>
            <tr th:each="i : ">
                <td th:text=""></td><td th:text=""></td>
                <td th:text=""></td><td th:text=""></td><td th:text=""></td>
                <td>
                    <a th:href="@{/inventory/edit/{id}(id=)}" class="btn">Edit</a>
                </td>
            </tr>
        </table>
    </div>
</body>
</html>''')

w(tm+'inventory/form.html', '''<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{layout :: head('Item Form')}"></head>
<body>
    <div th:replace="~{layout :: sidebar}"></div>
    <div class="content">
        <h1>Item Form</h1>
        <form th:action="" method="post">
            <div th:if="">Code: <input type="text" name="itemCode" required/></div>
            <div>Name: <input type="text" name="itemName" th:value="" required/></div>
            <div>Quantity: <input type="number" name="quantity" th:value="" required/></div>
            <div>Cost Price: <input type="number" step="0.01" name="costPrice" th:value="" required/></div>
            <div>Selling Price: <input type="number" step="0.01" name="sellingPrice" th:value="" required/></div>
            <button type="submit" class="btn">Save</button>
        </form>
    </div>
</body>
</html>''')

w(tm+'error.html', '''<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{layout :: head('Error')}"></head>
<body>
    <div th:replace="~{layout :: sidebar}"></div>
    <div class="content">
        <h1>Error</h1>
        <p class="alert" th:text=" ?: 'An unexpected error occurred.'"></p>
        <a href="/" class="btn">Back to Dashboard</a>
    </div>
</body>
</html>''')
