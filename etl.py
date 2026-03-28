import pandas as pd
import sqlite3

# -------------------------------
# EXTRACT
# -------------------------------
df = pd.read_csv("employees.csv")

# -------------------------------
# TRANSFORM
# -------------------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing salary values (fill with average)
df['salary'] = df['salary'].fillna(df['salary'].mean())

# Create new column: salary category
df['salary_category'] = df['salary'].apply(lambda x: "High" if x > 50000 else "Low")

# -------------------------------
# LOAD
# -------------------------------

# Save cleaned data to new CSV file
df.to_csv("cleaned_employees.csv", index=False)

# Load data into SQLite database
conn = sqlite3.connect("employee.db")
df.to_sql("employees", conn, if_exists='replace', index=False)

# -------------------------------
# OUTPUT
# -------------------------------

# Print first 5 rows
print("\nCleaned Data Preview:\n")
print(df.head())

print("\nETL Process Completed Successfully!")