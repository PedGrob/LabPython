# Input
input_total_bill = float(input("ยอดบิลรวม (บาท): "))  # รับยอดบิลรวม
number_of_people = int(input("จำนวนคนหาร: "))  # รับจำนวนคนหาร

# Calculations
amount_per_person = input_total_bill / number_of_people  # คำนวณจำนวนเงินต่อคน

# Print Result
print(f"\nยอดบิลรวม {input_total_bill:,.2f} บาท")
print(f"จำนวนคนหาร: {number_of_people} คน")
print(f"ยอดบิล {input_total_bill:,.2f} บาท หาร {number_of_people} คน ตกคนละ {amount_per_person:,.2f} บาท")