def calculate_salary(base_salary, ot_hours):
    ot_rate = 500 # ชั่วโมงละ 500 บาท
    ot_pay = ot_hours * ot_rate
    total_salary = base_salary + ot_pay
    if ot_hours > 10:
        bonus = 1000
        total_salary += bonus

    
    # หักประกันสังคม 5%
    social_security = total_salary * 0.05

    total_salary -= social_security

    return total_salary 

employees = [{"name":"สมชาย", "base_salary":20000, "ot_hours":5}, 
             {"name":"สมศรี", "base_salary":30000, "ot_hours":15}]

for emp in employees:
    final_salary = calculate_salary(emp["base_salary"], emp["ot_hours"])
    print(f"พนักงาน: {emp['name']}, เงินเดือนสุทธิ: {final_salary:,.2f} บาท")
