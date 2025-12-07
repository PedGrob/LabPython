# Input
salary = int(input("Enter your monthly salary (THB): "))
age_working = int(input("Enter your working age (years): "))

# Logic to determine year-end bonus
if age_working >= 1:
    grade = input("Enter your performance grade (A/B/C): ").upper()
    if grade == "A":
        bonus = salary * 2
    elif grade == "B":
        bonus = salary * 1
    else:
        bonus = salary * 0.5
    print(f"ยินดีด้วย! คุณได้รับโบนัสเป็นจำนวน {bonus} บาท")
else:
    print("คุณไม่มีสิทธิ์ได้รับโบนัส เนื่องจากอายุงานน้อยกว่าหรือเท่ากับ 1 ปี")