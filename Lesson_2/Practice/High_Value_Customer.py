# โจทย์: ฝ่ายการตลาดนิยาม "ลูกค้าพรีเมียม" ไว้ว่าต้องเข้าข่ายเงื่อนไขข้อใดข้อหนึ่ง ดังนี้:

# กลุ่มรวย: ยอดซื้อรวม (total_spend) มากกว่า 100,000 บาท
# กลุ่มขยันซื้อ: ยอดซื้อไม่ถึงแสนไม่เป็นไร แต่ต้องมาซื้อบ่อย (frequency) มากกว่า 50 ครั้ง และ เป็นสมาชิก (is_member)
# จงเขียน Logic เดียวให้ครอบคลุมเงื่อนไขนี้


# [ ]
# # ตัวอย่างผลลัพธ์
# Total Spend: 57200
# Frequency (times): 62
# Is Member (yes/no): yes
# Premium Status: True

# Input
total_spend = int(input("Total Spend: "))
frequency = int(input("Frequency (times): "))
is_member = input("Is Member (yes/no): ").lower()

# Logic to determine if the customer is a high-value customer
is_premium = (total_spend > 100000) or (frequency > 50 and is_member == "yes")

# Output
print("Premium Status:", is_premium)