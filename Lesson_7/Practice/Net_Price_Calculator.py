def calculate_final_price(price,discount,tax_rate):
    # คำนวณราคาหลังหักส่วนลด
    discounted_price = price - discount
    print(f"Log: Discounted price is {discounted_price}")
    
    # คำนวณภาษีมูลค่าเพิ่ม
    tax = discounted_price * tax_rate
    print(f"Log: Calculated tax is {tax}")
    
    # ราคาสุทธิหลังหักส่วนลดและบวกภาษี
    final_price = discounted_price + tax
    
    return final_price

products = [{"name":"Laptop", "price":1000},
            {"name":"Smartphone", "price":1000, "discount": 200, "tax_rate":0},]

for product in products:
    price = product["price"]
    discount = product.get("discount", 0)  # ถ้าไม่มีส่วนลด ให้ใช้ 0
    tax_rate = product.get("tax_rate", 0.07)  # ถ้าไม่มี tax_rate ให้ใช้ 7%
    
    net_price = calculate_final_price(price, discount, tax_rate)
    print(f"Product: {product['name']}, Net Price: {net_price:,.2f} USD")