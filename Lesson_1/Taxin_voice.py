# Input
name_input = input("ชื่อของลูกค้า: ") # รับชื่อลูกค้า
product_price = int(input("ราคาสินค้า: ")) # รับราคาสินค้า
total_quantity = int(input("จำนวนสินค้า: ")) # รับจำนวนสินค้า

#calculations Total, VAT and net balance
total_cost = product_price * total_quantity # ราคารวม
total_vat = total_cost * 0.07 # ภาษีมูลค่าเพิ่ม 7%
grand_total = total_cost + total_vat # ยอดสุทธิ

# Print Receipt
print('\n')
print("=" * 30)
print(f"ใบกำกับภาษีของ: \t{name_input:>8}")
print("=" * 30)
print(f"ราคารวม: \t{total_cost:>10,.2f} THB")
print(f"VAT (7%): \t{total_vat:>10,.2f} THB")
print("-" * 30)
print(f"ยอดสุทธิ: \t{grand_total:>12,.2f} THB")
print("=" * 30)
print("ขอบคุณที่ใช้บริการ")
