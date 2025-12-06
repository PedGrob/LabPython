x = str(3) # x will be '3' or "3"
y = int(3) # y will be 3
z = float(3) # z will be 3.0
print(x)
print(y)
print(z)
print("-" * 20) # Print a separator line

num_1 = 100
num_2 = "200"
print(num_1 + int(num_2))  # Convert num_2 to integer before addition
print(str(num_1) + num_2)  # Convert num_1 to string  
print("-" * 20) # Print a separator line

my_shop = "Super Coffee"
sales = 15000

# แบบเดิม
print("รายงานสรุปของร้าน: " + my_shop + "\nยอดขายวันนี้รวมทั้งหมด: " + str(sales))
print("="*20)
# แบบ f-string
print(f"รายงานสรุปของร้าน: {my_shop}\nยอดขายวันนี้รวมทั้งหมด: {sales:.2f} บาท") 
print(f"รายงานสรุปของร้าน: {my_shop}\nยอดขายวันนี้รวมทั้งหมด: {sales:,} บาท")
print(f"รายงานสรุปของร้าน: {my_shop}\nยอดขายวันนี้รวมทั้งหมด: {sales:,.2f} บาท")  
print("-" * 20) # Print a separator line

revenue = 1234567.891234
vat = 0.07

tax_amount = revenue * vat

print(f"ภาษีที่คำนวณได้:\t{tax_amount:>15,.2f} บาท")
print("-" * 20) # Print a separator line
# แบบจัดระเบียบแล้ว (สังเกตหลังเครื่องหมาย :)
print(f"ยอดรายได้ตั้งต้น:\t{revenue:>15,.2f} บาท")
print(f"ภาษีที่ต้องจ่ายจริง:\t{tax_amount:>15,.2f} บาท")
