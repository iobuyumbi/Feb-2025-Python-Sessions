import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset (csv file)
# df = pd.read_csv('sales_data.csv')
df = pd.read_csv(r'C:\Users\HOME\OneDrive\PLP\Python PLP\Feb-2025-Python-Sessions\Python Data Analysis Challenge\sales_data.csv')


# 2. Calculate total revenue
total_revenue = df['Revenue ($)'].sum()

# 3a. Find best-selling product
best_selling = df.groupby('Product')['Quantity Sold'].sum().idxmax()
best_selling_qty = df.groupby('Product')['Quantity Sold'].sum().max()

# 3b. Find worst-selling product
worst_selling = df.groupby('Product')['Quantity Sold'].sum().idxmin()
worst_selling_qty = df.groupby('Product')['Quantity Sold'].sum().min()

# 4. Find day with highest sales revenue
highest_sales_day = df.groupby('Date')['Revenue ($)'].sum().idxmax()

# 5. Save insights to a text file
with open('sales_insights.txt', 'w') as file:
    file.write(f'Total Revenue: ${total_revenue}\n')
    file.write(f'Best Selling Product: {best_selling} (Quantity Sold: {best_selling_qty})\n')
    file.write(f'Worst Selling Product: {worst_selling} (Quantity Sold: {worst_selling_qty})\n')
    file.write(f'Day with Highest Sales Revenue: {highest_sales_day}\n')

# 6. Print results in a friendly format
print("Sales Summary")
print("--------------")
print(f'Total Revenue: ${total_revenue:.2f}')
print(f'Best Selling Product: {best_selling} (Quantity Sold: {best_selling_qty})')  
print(f'Worst Selling Product: {worst_selling} (Quantity Sold: {worst_selling_qty})')
print(f'Day with Highest Sales Revenue: {highest_sales_day}')


# 7. Visualize sales trends
# Total revenue per day
daily_revenue = df.groupby('Date')['Revenue ($)'].sum()

plt.figure(figsize=(10, 5))
daily_revenue.plot(kind='line', marker='o', color='teal')
plt.title('Daily Revenue Trend')    
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.tight_layout()
plt.savefig('daily_revenue_trend.png')
plt.show()

