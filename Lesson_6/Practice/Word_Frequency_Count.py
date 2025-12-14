feedbacks = ["Good", "Bad", "Good", "Excellent", "Bad", "Good"]
frequency = {}
for feedback in feedbacks:
    frequency[feedback] = frequency.get(feedback, 0) + 1
print(f"Feedback Count: {frequency}")