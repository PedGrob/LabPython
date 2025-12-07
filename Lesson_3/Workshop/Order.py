# Input
print("--- Shipping Cost Calculator ---")
weight = int(input("ใส่ค่าน้ำหนักของสินค้า (กิโลกรัม): "))

# Logic to determine shipping cost
if weight <= 20:
    print("สามารถส่งสินค้าได้\n")
    is_vip = input("เป็นลูกค้า VIP หรือไม่? (yes/no): ").lower()
    print(f"น้ำหนัก {weight} กิโลกรัม น้ำหนักอยู่ในเกณฑ์รับส่ง")
    if is_vip == "yes":
        shipping_cost = 0
    else:
        if weight <= 1:
            shipping_cost = 40
        elif weight <= 5:
            shipping_cost = 80
        elif weight > 5:
            shipping_cost = 150
    print("-" * 20)
    print(f"ค่าจัดส่ง: {shipping_cost} บาท")

else:
    print("ไม่สามารถส่งสินค้าได้ เนื่องจากน้ำหนักเกิน 20 กิโลกรัม")
    shipping_cost = None

