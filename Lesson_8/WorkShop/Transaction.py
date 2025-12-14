alert_msg = "TXN_ID:8854 | Date:2025-12-01 | Status:PENDING"
# เจ้านายต้องการรู้ว่า "รายการนี้ค้างมากี่วันแล้ว?" (นับจากวันนี้)
# โจทย์:
# แยกก้อนวันที่ออกมาจากข้อความ
# เอาคำว่า " Date:" ออก ให้เหลือแค่ตัวเลขวันที่
# แปลงเป็น Datetime
# คำนวณหาจำนวนวันที่ค้าง
from datetime import datetime, timedelta

# แยกวันที่จาก alert_msg
date_str = alert_msg.split("Date:")[1].split(" |")[0]
date_obj = datetime.strptime(date_str, "%Y-%m-%d")

# คำนวณจำนวนวันที่ค้าง
today = datetime.now()
print(f"วันนี้วันที่: {today.strftime('%Y-%m-%d')}")
days_pending = (today - date_obj).days
years_pending = days_pending // 365
months_pending = (days_pending % 365) // 30

print(f"รายการนี้ค้างมากี่วันแล้ว: {days_pending} วัน")
print(f"หรือประมาณ: {years_pending} ปี {months_pending} เดือน")