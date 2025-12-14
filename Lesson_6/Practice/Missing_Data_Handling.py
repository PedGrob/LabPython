users = [
  {"id": 1, "name": "Somchai", "phone": "081-111-2222"},
  {"id": 2, "name": "Somsri"}, # ผู้ใช้คนนี้ไม่มี key 'phone'
  {"id": 3, "name": "Somkiat", "phone": "089-999-8888"}
]
for user in users:
    phone = user.get("phone", "N/A")  # ใช้ .get() เพื่อดึงค่า 'phone' ถ้าไม่มีให้ใช้ "N/A"
    print(f"User ID: {user['id']}, Name: {user['name']}, Phone: {phone}")