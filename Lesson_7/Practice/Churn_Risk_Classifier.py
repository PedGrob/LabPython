def check_churn_rick(day):
    if day > 60:
        return "High Risk"
    elif day > 30:
        return "Medium Risk"
    else:
        return "Low Risk"
users = [{"username":"User A", "last_login":10},
         {"username":"User B", "last_login":45},
         {"username":"User C", "last_login":90}]

for user in users:
    risk = check_churn_rick(user["last_login"])
    print(f"Username: {user['username']}, Last Login: {user['last_login']} days ago, Churn Risk: {risk}")