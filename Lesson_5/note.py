# รายชื่อลูกค้า 3 คน
customers = ["Alice", "Bob", "Charlie"]

print("=== วิธีแบบถึก (Manual) ===")
# ต้องพิมพ์ทีละบรรทัด ถ้ามี 100 คนก็ต้องพิมพ์ 100 บรรทัด
print(f"สวัสดีคุณ {customers[0]}")
print(f"สวัสดีคุณ {customers[1]}")
print(f"สวัสดีคุณ {customers[2]}")

print("\n=== วิธี Loop (Automatic) ===")
# เขียนแค่นี้ ไม่ว่าลูกค้าจะมีกี่คน ก็พิมพ์ครบทุกคน
for customer in customers:
  print(f"สวัสดีคุณ {customer}")