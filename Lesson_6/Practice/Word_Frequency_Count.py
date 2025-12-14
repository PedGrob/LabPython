feedbacks = ["Good", "Bad", "Good", "Excellent", "Bad", "Good"]
frequency = {}
for feedback in feedbacks:
    frequency[feedback] = frequency.get(feedback, 0) + 1 # feedback เป็น key ถ้ายังไม่มีให้เริ่มที่ 0 แล้วบวกเพิ่ม 1
print(f"Feedback Count: {frequency}")