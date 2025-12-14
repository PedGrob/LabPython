def calculate_tax(income):
  tax = income * 0.10

  # ส่งค่าคืนทันที Eject!
  print(f"Log: Calculated tax for income {income}")
  return tax

  # โค้ดส่วนนี้จะกลายเป็น Unreachable Code ทันที
  # Python จะจบการทำงานของฟังก์ชันทันที ไม่มีการ print ออกมา
  print(f"Log: Calculated tax for income {income}")

# ทดสอบ
my_tax = calculate_tax(50000)
print(f"Tax is: {my_tax}")
