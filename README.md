# 📦 Sales Order Data Engineering Project

This project is our first end-to-end Data Engineering application. It includes a full **ETL (Extract, Transform, Load)** pipeline using **Pandas** and **SQL**, along with a fully interactive **dashboard built in Dash (Plotly)**.

We built this project to gain practical experience in preparing for internship opportunities in the **Data and AI** domain.

---

## 🚀 Project Features

- ✅ Data transformation using Pandas
- ✅ Region assignment based on city mapping
- ✅ Revenue, Order, and Monthly Aggregations
- ✅ Data loading into MySQL using SQLAlchemy
- ✅ Dashboard built with Dash & Plotly
- ✅ Interactive charts and KPI cards

---

## 🧰 Tech Stack

| Tool         | Purpose                          |
|--------------|----------------------------------|
| Python       | Core programming language        |
| Pandas       | Data cleaning and transformation |
| SQLAlchemy   | Loading data into MySQL          |
| MySQL        | Data storage and querying        |
| Dash (Plotly)| Dashboard development            |

---

## 🔄 ETL Pipeline (etl_pipeline.py)

### ✅ **Extract**
- Source: CSV file with sales order data (`sales_orders_1000.csv`)

### 🔧 **Transform**
- Calculated `Total_Price` (Quantity × Price)
- Converted `OrderDate` to datetime
- Extracted month name from `OrderDate`
- Mapped `City` to `Region` using a custom dictionary
- Rearranged columns for better readability

### 🧩 **Load**
- Used **SQLAlchemy** to connect and load the data into a MySQL database named `ordersdb`.

---

## 📊 Dashboard (app.py)

The dashboard provides interactive insights into sales data:

- 💰 **Total Revenue**
- 📦 **Total Orders**
- 📈 **Bar Chart:** Revenue by Month
- 🧭 **Pie Chart:** Orders by Region
- 🧾 **Scatter Plot:** City vs Total Price with Quantity & Order Date

> The dashboard opens automatically in the browser at `http://127.0.0.1:8050/`
