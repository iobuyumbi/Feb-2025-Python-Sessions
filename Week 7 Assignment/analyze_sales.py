# analyze_sales.py

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style='whitegrid')

# Task 1: Load and Explore the Dataset
try:
    # Load dataset (assuming the file is named 'sales_data.csv')
    df = pd.read_csv('sales_data.csv')

    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ File 'sales_data.csv' not found. Please ensure the dataset is in the correct path.")
    exit()

# Display the first few rows of the dataset
print("🔍 First 5 rows:\n", df.head())

# Task 1: Explore the structure of the dataset
print("\n📊 Data types:\n", df.dtypes)
print("\n🧼 Missing values:\n", df.isnull().sum())

# Clean the dataset - Drop rows with missing values (or fill them if necessary)
df.dropna(inplace=True)  # Drop rows with missing values

# Task 2: Basic Data Analysis
# Compute basic statistics for numerical columns
print("\n📈 Summary Statistics:\n", df.describe())

# Perform groupings based on 'Product' and calculate the total revenue per product
grouped = df.groupby('Product')['Revenue ($)'].sum()
print("\n🔎 Total Revenue by Product:\n", grouped)

# Find the best-selling product based on 'Quantity Sold'
best_selling_product = df.groupby('Product')['Quantity Sold'].sum().idxmax()
best_selling_product_quantity = df.groupby('Product')['Quantity Sold'].sum().max()

# Find the day with the highest sales (highest total revenue)
df['Date'] = pd.to_datetime(df['Date'])  # Ensure the 'Date' column is in datetime format
highest_sales_day = df.groupby('Date')['Revenue ($)'].sum().idxmax()
highest_sales_day_revenue = df.groupby('Date')['Revenue ($)'].sum().max()

# Task 3: Data Visualization

# 1. Line chart - Show trends in revenue over time
plt.figure(figsize=(10, 6))
df.groupby('Date')['Revenue ($)'].sum().plot(kind='line', marker='o', color='blue')
plt.title('Revenue Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar chart - Show total revenue by product
plt.figure(figsize=(10, 6))
grouped.plot(kind='bar', color='orange')
plt.title('Total Revenue by Product')
plt.ylabel('Revenue ($)')
plt.xlabel('Product')
plt.tight_layout()
plt.show()

# 3. Histogram - Distribution of revenue
plt.figure(figsize=(10, 6))
df['Revenue ($)'].plot(kind='hist', bins=10, color='green', edgecolor='black')
plt.title('Revenue Distribution')
plt.xlabel('Revenue ($)')
plt.tight_layout()
plt.show()

# 4. Scatter plot - Visualize the relationship between Quantity Sold and Revenue
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Quantity Sold', y='Revenue ($)', hue='Product')
plt.title('Quantity Sold vs Revenue')
plt.xlabel('Quantity Sold')
plt.ylabel('Revenue ($)')
plt.legend(title='Product')
plt.tight_layout()
plt.show()

# Print insights
print("\n📝 Insights:")
print(f"Best-selling Product: {best_selling_product} ({best_selling_product_quantity} units sold)")
print(f"Highest Sales Day: {highest_sales_day} with ${highest_sales_day_revenue} in revenue")

