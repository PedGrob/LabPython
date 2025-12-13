cart_prices = [100, 250, 500, 50, 1200]
total_price = 0
count_items = 0
promotion = 0 # ส่วนลด 10% สำหรับสินค้าที่มีราคามากกว่า 2000 บาท

for price in cart_prices:
    print(f"ยิงบาร์โค้ดสินค้า ราคา {price:,.2f} บาท")
    total_price = total_price + price
    count_items = count_items + 1
    if total_price > 2000:
        promotion = 0.1
        discount = total_price * promotion
            


print("=" * 30)
print(f"สรุป: ซื้อสินค้า {count_items} ชิ้น | ราคารวม: {total_price:,.2f} บาท")
print(f"โปรโมชั่น: ลดราคา {int(promotion * 100)}% (-{discount:,.2f} บาท) เมื่อราคารวมเกิน 2,000 บาท")
print("=" * 30)
print(f"ยอดสุทธิที่ต้องชำระ: {(total_price - discount):,.2f} บาท")