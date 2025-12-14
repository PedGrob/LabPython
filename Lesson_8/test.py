from datetime import datetime, timedelta

now = datetime.now()
print(f"วันนี้: {now.strftime('%d/%m/%Y')} {now.strftime('%I:%M %p')}")

# 3. หา "เมื่อวาน" (ใช้บ่อยมากตอนดึง Data ย้อนหลัง)
yesterday = now - timedelta(days=1)
print(f"เมื่อวาน: {yesterday.strftime('%d/%m/%Y')} {yesterday.strftime('%I:%M %p')}")

# 4. หา "อาทิตย์หน้า"
deadline = now + timedelta(weeks=1)
print(f"ครบกำหนด: {deadline.strftime('%d/%m/%Y')} {deadline.strftime('%I:%M %p')}")

# 5. อีก 2 ชั่วโมงข้างหน้า
next_2_hours = now + timedelta(hours=2)
print(f"อีก 2 ชม.: {next_2_hours.strftime('%d/%m/%Y')} {next_2_hours.strftime('%I:%M %p')}")