daily_sales = [1000, 2000, 1500, 3000, 2500]
print(daily_sales)

data = ["Somchai", 35, True] # ชื่อ, อายุ, สถานะสมาชิก

stock_prices = [150.5, 152.0, 149.5, 155.0, 160.0]
# ดึงข้อมูลตัวแรก (Index 0)
first_price = stock_prices[0]
print(f"ราคาเปิดตลาด (ตัวแรก): {first_price}")

# ดึงข้อมูลตัวที่ 3 (Index 2)
third_price = stock_prices[2]
print(f"ราคาช่วงสาย (ตัวที่ 3): {third_price}")

# ดึงราคาปิดตลาด (ตัวสุดท้าย) โดยไม่ต้องนับว่ามีกี่ตัว
last_price = stock_prices[-1]
print(f"ราคาปิดตลาด (ล่าสุด): {last_price}")

customers = ["Alice", "Bob", "Charlie", "David", "Eve"]

# เอา 3 คนแรก (Index 0, 1, 2)
top_3 = customers[0:3]
print(f"Top 3 Customers: {top_3}")

top_5 = customers[:5]
print(f"Top 5 Customers: {top_5}")

# เอาตั้งแต่คนที่ 2 จนจบ (Index 2 ถึงตัวสุดท้าย)
# ทริค: ถ้าไม่ใส่เลขหลัง colon แปลว่า "ยาวไปจนจบ"
others = customers[2:]
print(f"ลูกค้าที่เหลือ: {others}")

products = ["Coke", "Pepsi", "Fanta"]
print(f"สินค้าเดิม: {products}")

# 1. มีสินค้าใหม่เข้ามา (Add)
products.append("Sprite")
print(f"หลังเพิ่ม: {products}")

# 2. สินค้าเลิกจำหน่าย (Delete)
products.remove("Pepsi")
print(f"หลังลบ: {products}")

# 3. แก้ไขข้อมูล (Update)
# เปลี่ยน Coke (ตัวที่ 0) เป็น Coke Zero
products[0] = "Coke Zero"
print(f"หลังแก้ไข: {products}")