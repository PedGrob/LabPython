# Input
input_width = float(input("กรอกความกว้าง (cm): "))  # รับความกว้างของสี่เหลี่ยมจัตุรัส
input_height = float(input("กรอกความยาว (cm): "))  # รับความสูงของสี่เหลี่ยมจัตุรัส

# Calculations
area_square = input_width * input_height  # คำนวณพื้นที่สี่เหลี่ยมจัตุรัส

# Print Result
print(f"\nสี่เหลี่ยมกว้าง {input_width:,.2f} cm และสูง {input_height:,.2f} cm มีพื้นที่ {area_square:,.2f} ตารางเซนติเมตร")