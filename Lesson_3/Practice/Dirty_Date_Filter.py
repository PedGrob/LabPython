# Input
age_input = input("Enter your age: ").strip() 

# Logic
if age_input == "": 
    print("Missing Data (ไม่ได้กรอกอะไรเลย)")
else:
    age = int(age_input) 
        
    if age < 0 or age > 120: 
        print("Out of Range")
    else:
        print("Valid Data")
            
    