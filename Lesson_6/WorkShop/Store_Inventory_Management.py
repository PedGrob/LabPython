# === พื้นที่เขียนโค้ด ===

inventory = {"Coke": 100, "Pepsi": 50, "Water": 200}
new_lot = {"Coke": 50, "Fanta": 100}

print(f"Original Stock: {inventory}")

# 1. Update Stock Logic
# Loop อ่าน new_lot ทีละตัว (item)
#   ถ้ามี key ใน inventory -> บวกเพิ่ม
#   ถ้าไม่มี -> สร้างใหม่

for item, qty in new_lot.items():
    if item in inventory:
        inventory[item] = inventory[item] + qty
    else:
        inventory[item] = qty

print(f"Current Stock: {inventory}")

# 2. Check Low Stock
print("\n=== Low Stock Alert ===")
# Loop อ่าน inventory (items)
#   ถ้า value < 100 -> Print Alert

for item, qty in inventory.items():
    if qty < 100:
        print(f"Alert! Low stock for {item}: {qty} left")

# 3. Final Report
print("\n=== Final Inventory Report ===")
# Loop อ่าน inventory (items)
#   Print สินค้า และ จำนวนคงเหลือ
for item, qty in inventory.items():
    print(f"Item: {item} | Quantity: {qty}")

# === จบพื้นที่เขียนโค้ด ===