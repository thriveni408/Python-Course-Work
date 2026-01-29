import numpy as np
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta
from collections import Counter


# 1. Generate Sales Data
product_categories = ["Electronics", "Clothing", "Groceries", "Furniture", "Toys"]

# Generate random dates over 6 months
start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 6, 30)

num_transactions = 1000  # total transactions
sales_data = []

for _ in range(num_transactions):
    # Random date
    delta_days = (end_date - start_date).days
    random_date = start_date + timedelta(days=random.randint(0, delta_days))
    
    # Random category, units, price
    category = random.choice(product_categories)
    units_sold = random.randint(1, 100)
    price_per_unit = round(random.uniform(5, 500), 2)
    total_sales = round(units_sold * price_per_unit, 2)
    
    sales_data.append([random_date, category, units_sold, price_per_unit, total_sales])


# 2. Convert to structured arrays for analysis

dates = np.array([row[0] for row in sales_data])
categories = np.array([row[1] for row in sales_data])
units = np.array([row[2] for row in sales_data])
prices = np.array([row[3] for row in sales_data])
totals = np.array([row[4] for row in sales_data])
# 3. Data Analysis

# Total revenue
total_revenue = np.sum(totals)

# Revenue per month
months = np.array([d.strftime("%B") for d in dates])
unique_months = sorted(list(set(months)), key=lambda m: datetime.strptime(m, "%B").month)
monthly_revenue = {month: np.sum(totals[months == month]) for month in unique_months}

# Best-selling category
category_sales = {cat: np.sum(totals[categories == cat]) for cat in product_categories}
best_category = max(category_sales, key=category_sales.get)

# Peak sales month
peak_month = max(monthly_revenue, key=monthly_revenue.get)

# Average sales per day
days = np.array([d.date() for d in dates])
unique_days = np.unique(days)
daily_totals = [np.sum(totals[days == day]) for day in unique_days]
average_daily_sales = np.mean(daily_totals)


# 4. Display Overall Summary

print("----- Overall Sales Summary -----")
print(f"Total Sales Revenue: ${total_revenue:,.2f}")
print(f"Best-Selling Category: {best_category}")
print(f"Peak Sales Month: {peak_month}")
print(f"Average Daily Sales: ${average_daily_sales:,.2f}\n")


# 5. User Interaction

month_input = input("Enter a month to analyze (e.g., January, February): ").capitalize()

if month_input in unique_months:
    month_indices = months == month_input
    month_total_sales = np.sum(totals[month_indices])
    month_categories = categories[month_indices]
    month_category_counts = Counter(month_categories)
    best_product = month_category_counts.most_common(1)[0][0]
    num_transactions_month = np.sum(month_indices)
    
    print(f"\n--- Sales Report for {month_input} ---")
    print(f"Total Sales: ${month_total_sales:,.2f}")
    print(f"Best-Selling Product Category: {best_product}")
    print(f"Number of Transactions: {num_transactions_month}\n")
else:
    print("Invalid month entered!")


# 6. Visualization


# 6.1 Line Chart: Sales trends over time
plt.figure(figsize=(10,5))
daily_sales_sorted = sorted(zip(unique_days, daily_totals))
dates_sorted, totals_sorted = zip(*daily_sales_sorted)
plt.plot(dates_sorted, totals_sorted, marker='o')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6.2 Bar Chart: Total sales per category
plt.figure(figsize=(8,5))
plt.bar(category_sales.keys(), category_sales.values(), color='skyblue')
plt.title("Total Sales per Product Category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")
plt.show()

# 6.3 Pie Chart: Sales distribution among categories
plt.figure(figsize=(7,7))
plt.pie(category_sales.values(), labels=category_sales.keys(), autopct='%1.1f%%', startangle=140)
plt.title("Sales Distribution by Category")
plt.show()

# 6.4 Histogram: Distribution of sales transactions
plt.figure(figsize=(8,5))
plt.hist(totals, bins=20, color='lightgreen', edgecolor='black')
plt.title("Distribution of Sales Transactions")
plt.xlabel("Sales Amount ($)")
plt.ylabel("Number of Transactions")
plt.show()
