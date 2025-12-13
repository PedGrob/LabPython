raw_sales = [1200, -500, 3500, 0, 800, 4000, -99]

total_clean_sales = 0
valid_orders = 0


for sale in raw_sales:
    if sale > 0:
        print(f"ประมวลผลยอดขาย: {sale:,}")
        total_clean_sales = total_clean_sales + sale
        valid_orders = valid_orders + 1
    else:
        print(f"ข้อมูลที่ไม่ถูกต้อง: {sale:,}")
        
print("=== สรุปยอดขาย ===")
print(f"จำนวนคำสั่งซื้อที่ถูกต้อง: {valid_orders} รายการ จาก {len(raw_sales)} รายการ")
print(f"ยอดขายรวมที่ถูกต้อง: {total_clean_sales:,} บาท")