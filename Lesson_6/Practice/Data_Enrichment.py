# สถานการณ์: คุณมีข้อมูลพนักงาน (List of Dicts) และเจ้านายต้องการให้ "ตัดเกรด" พนักงานทุกคนเพิ่มเข้าไปในข้อมูลเดิม

# คะแนน >= 80 -> Grade A
# คะแนน < 80 -> Grade B
employees = [
  {"name": "Alice", "score": 85},
  {"name": "Bob", "score": 72},
  {"name": "Charlie", "score": 90}
]
for employee in employees:
    if employee["score"] >= 80:
        employee["grade"] = "A"
    else:
        employee["grade"] = "B"
    print(f"Updated Employee: {employee}")
print("\nFinal Employee Data:")
print(employees)


