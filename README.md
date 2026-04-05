# Employee Data ETL Pipeline & Analysis

## 📌 Project Overview
This project demonstrates an ETL (Extract, Transform, Load) pipeline built using Python and SQL. The objective is to process raw employee data, clean it, and store it in a structured database for analysis.

---

## ⚙️ Technologies Used
- Python (Pandas)
- SQL (SQLite)
- VS Code

---

## 🔄 ETL Process

### 1. Extract
- Loaded raw employee data from CSV file using Pandas

### 2. Transform
- Removed duplicate records
- Handled missing values
- Standardized data formats
- Created a new column `salary_category` for better analysis

### 3. Load
- Stored cleaned data into SQLite database
- Exported processed data into a new CSV file

---

## 📊 Key Features
- Data cleaning and preprocessing
- Feature engineering (salary_category)
- SQL-based data analysis
- Structured data storage using SQLite

---

## 📁 Project Structure
Employee-Data-Project/
│
├── employees.csv
├── cleaned_employees.csv
├── etl.py
├── queries.sql
└── employee.db

---

## ▶️ How to Run

1. Install required library:
pip install pandas

2. Run the ETL script:
python etl.py

---

## 📈 Sample SQL Queries
- Department-wise average salary
- Employee count per department
- High salary employees

---

## 🎯 Conclusion
This project demonstrates the end-to-end workflow of a basic data engineering pipeline, including data extraction, transformation, and loading into a database for analysis.