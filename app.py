import mysql.connector
import pandas as pd

# DB connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sujalsingh26",
    database="sales_db"
)
df = pd.read_sql("SELECT product, quantity, price_per_unit FROM sales", conn)
conn.close()

# Total revenue per product
df['revenue'] = df['quantity'] * df['price_per_unit']
summary = df.groupby('product')[['quantity','revenue']].sum().sort_values('revenue', ascending=False)

print("=== Sales Summary per Product ===")
print(summary, "\n")

print(f"Overall Revenue: INR {summary['revenue'].sum()}")
best = summary['quantity'].idxmax()
print(f"Best Selling Product: {best} ({summary.loc[best,'quantity']} units)")
worst = summary['revenue'].idxmin()
print(f"Lowest Revenue Product: {worst} (INR {summary.loc[worst,'revenue']})")