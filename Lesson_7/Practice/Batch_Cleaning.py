def clean_salary(salary_str):
    # ลบสัญลักษณ์ $ และ , ออก
    cleaned = salary_str.replace("$", "").replace(",", "")
    print(f"Processed: {salary_str} -> {cleaned}")
    return int(cleaned)

raw_salaries = ["$20,000", "$45,000", "$18,500"]

clean_list = []

for raw_salary in raw_salaries:
    clean_salary_value = clean_salary(raw_salary)
    clean_list.append(clean_salary_value)

print(f"Clean Salary List: {clean_list}")