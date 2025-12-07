# Input
sales_data = [1200, 1500, 900, 2000, 50, 3000]
print(f"Original Data: {sales_data}")
# ลบยอกขาย 50 ออก
sales_data.remove(50)

# เพิ่มยอดขายวันอาทิตย์ 2500 เข้าไป
sales_data.append(2500)
print(f"Cleaned Data: {sales_data}")
# นับจำนวนวันที่ขาย
num_days = len(sales_data)

# หายอดขายรวมทั้งสัปดาห์
total_sales = sum(sales_data)

# หายอดขายสูงที่สุด (Max)
max_sales = max(sales_data)

# หายอดขายต่ำที่สุด (Min)
min_sales = min(sales_data)

# Report
print("\n--- Weekly Sales Report ---")
print(f"Total Selling Days: {num_days} days")
print(f"Total Revenue: \t{total_sales:,.2f} Baht")
print(f"Highest Sale: \t{max_sales:,.2f} Baht")
print(f"Lowest Sale: \t{min_sales:.2f} Baht")
print(f"Average/Day: \t{total_sales / num_days:,.2f} Baht")