import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Task 2: A Line Plot with Pandas
db_path = 'db/lesson.db'

conn = sqlite3.connect(db_path)

query = """
SELECT 
    o.order_id,
    SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

# Load data into a DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

# ADD CUMULATIVE TOTAL COLUMN using apply() (as shown by instructor)
def cumulative(row):
    totals_above = df['total_price'][0:row.name + 1]
    return totals_above.sum()
df['cumulative'] = df.apply(cumulative, axis=1)


# Another option to get cumulative total 
#df['cumulative'] = df['total_price'].cumsum()

print("Cumulative Revenue Data (First 10 rows):")
print(df.head(10))

print(f"\nTotal Orders: {len(df)}")
print(f"Final Cumulative Revenue: ${df['cumulative'].iloc[-1]:,.2f}")


# Create line plot
plt.figure(figsize=(12, 7))
df.plot(x='order_id', y='cumulative', kind='line', marker='o')
plt.title('Cumulative Revenue by Order ID')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue')
plt.grid()
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))  # Format y-axis as currency
plt.show()