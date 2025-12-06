# โจทย์: ร้านค้าต้องการแจกคูปองส่วนลด โดยมีเงื่อนไขว่าลูกค้าจะได้รับคูปองก็ต่อเมื่อ:

# เป็นสมาชิก (is_member = "yes") และ มียอดซื้อเกิน 1,000 บาท
# หรือ เป็นลูกค้าใหม่ (is_new = "yes") (ลูกค้าใหม่แจกเลย ไม่สนยอดซื้อ)
# จงเขียน Logic เพื่อสรุปผลว่าลูกค้าจะได้รับคูปองหรือไม่ (Get Coupon: True/False)

# # ตัวอย่างผลลัพธ์
# Total Spend: 1200
# Is Member? (yes/no): yes
# Is New Customer? (yes/no): no
# Get Coupon: True

# Input
total_spend = int(input("Total Spend: "))
is_member = input("Is Member? (yes/no): ").lower()
is_new = input("Is New Customer? (yes/no): ").lower()

# Logic to determine if the customer gets a coupon
get_coupon = (is_member == "yes" and total_spend > 1000) or (is_new == "yes")

# Output
print("Get Coupon:", get_coupon)
