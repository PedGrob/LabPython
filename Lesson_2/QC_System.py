# ตัวอย่างระบบตรวจสอบสินค้า (QC System)
standard_weight = 500  # น้ำหนักมาตรฐาน 500 กรัม
actual_weight = 495    # น้ำหนักจริงที่ชั่งได้

# ตรวจสอบว่าน้ำหนักต่ำกว่าเกณฑ์หรือไม่?
is_underweight = actual_weight < standard_weight
print(f"สินค้าตกเกรด (น้ำหนักน้อยกว่ามาตรฐาน): {is_underweight}")  # จะได้ True

# ตรวจสอบว่าน้ำหนักตรงตามมาตรฐานหรือไม่?
is_perfect = actual_weight == standard_weight
print(f"สินค้าน้ำหนักตรงตามมาตรฐาน: {is_perfect}")     # จะได้ False