# Input order details
print("=== ระบบคัดกรอง Oder สินค้า ===")
item_name = input("ชื่อสินค้า: ")
current_stock = int(input("จำนวนสินค้าในสต็อก: "))
order_qty = int(input("จำนวนสินค้าที่สั่งซื้อ: "))
is_vip = input("ลูกค้าเป็นสมาชิก VIP หรือไม่ (YES/NO): ").upper() == "YES"

# 1. ตรวจสอบจำนวนสั่งซื้อพื้นฐาน (ต้อง > 0 เสมอ)
valid_quantity = (order_qty > 0)

# 2. ตรวจสอบเงื่อนไขการอนุมัติ (VIP หรือ Stock พอ)
approval_condition = is_vip or (order_qty <= current_stock)

# 3. สรุปผล Order: ต้องผ่านทั้งสองเงื่อนไข (Quantity และ Approval)
order_confirm = valid_quantity and approval_condition

# print results
print("\n--- ผลการคัดกรอง ---")
print(f"ชื่อสินค้า: {item_name}")
print(f"จำนวนสินค้าที่สั่งซื้อ: {order_qty}")
print(f"สถานะลูกค้า VIP: {is_vip}")
print("-" * 20)
print(f"ยืนยัน order หรือไม่?: {order_confirm}")
print(f"-" * 20)