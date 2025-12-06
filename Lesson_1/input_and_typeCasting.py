# โปรแกรมรับข้อมูลของพนักงานใหม่
print("--- Employee Registration ---")

emp_name = input("กรุณากรอกชื่อพนักงาน: ")
department = input("กรุณากรอกแผนก: ")
price_per_unit = float(input("ระบุราคาสินค้า (บาท): ")) # ใช้ float เผื่อมีจุดทศนิยม
quantity = int(input("ระบุจำนวนสินค้า (ชิ้น): "))       # ใช้ int เพราะจำนวนชิ้นมักเป็นจำนวนเต็ม

total = price_per_unit * quantity

print("บันทึกข้อมูลสำเร็จ!")
print("ยินดีต้อนรับคุณ " + emp_name + " แห่งแผนก " + department)
print(f"ราคารวมทั้งหมดคือ: {total:>10,.2f} บาท")