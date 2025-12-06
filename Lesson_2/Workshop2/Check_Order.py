# Input order details
print("=== ระบบคัดกรอง Oder สินค้า ===")
item_name = input("ชื่อสินค้า: ")
current_stock = int(input("จำนวนสินค้าในสต็อก: "))
order_qty = int(input("จำนวนสินค้าที่สั่งซื้อ: "))
is_vip = input("ลูกค้าเป็นสมาชิก VIP หรือไม่ (YES/NO): ") == "YES"

# Check stock availability
stock_check = not is_vip and ((order_qty <= current_stock) > 0)

# Check VIP status
vip_check = is_vip and (order_qty > 0)

# comfime order
order_confirm = stock_check or vip_check

# print results
print("\n--- ผลการคัดกรอง ---")
print(f"ชื่อสินค้า: {item_name}")
print(f"จำนวนสินค้าที่สั่งซื้อ: {order_qty}")
print(f"สถานะลูกค้า VIP: {vip_check}")
print("-" * 20)
print(f"ยืนยัน order หรือไม่?: {order_confirm}")
print(f"-" * 20)