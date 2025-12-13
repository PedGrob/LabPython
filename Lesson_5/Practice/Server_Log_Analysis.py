logs = [200, 200, 404, 500, 200, 404, 200, 301, 500, 200]

failsafe_counts = 0

for log in logs:
    print(f"Processing log entry: {log}")
    if log == 200:
        print("Status: OK")
    elif log == 301:
        print("Status: Moved Permanently")
        failsafe_counts = failsafe_counts + 1
    elif log == 404:
        print("Status: Not Found")
        failsafe_counts = failsafe_counts + 1
    elif log == 500:
        print("Status: Internal Server Error")
        failsafe_counts = failsafe_counts + 1
    else:
        print("Status: Unknown")

print(f"พบจำนวน failsafe errors ทั้งหมด: {failsafe_counts} รายการ จาก {len(logs)} รายการ")
