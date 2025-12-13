pm_values = [25, 50, 0, 30, -1, 45, 0]

total_pm = 0
count_valid = 0
list_count_valid = []
for pm in pm_values:
    if pm > 0:
        total_pm = total_pm + pm
        count_valid = count_valid + 1
        list_count_valid.append(pm)
    

if count_valid > 0:
    average_pm = total_pm / count_valid
    print(f"ค่าที่อ่านได้ {count_valid} ค่า จากทั้งหมด {len(pm_values)} ค่า")
    print(f"ค่าที่ถูกต้อง: {list_count_valid}")
    print(f"ค่าเฉลี่ยของฝุ่น PM2.5: {average_pm:.2f}")
else:
    print("ไม่มีข้อมูลที่ถูกต้อง")