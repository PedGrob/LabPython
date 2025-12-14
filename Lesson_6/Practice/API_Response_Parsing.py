# สถานการณ์: เมื่อดึงข้อมูลจากเว็บ (API) ข้อมูลมักจะมาในรูปแบบ Nested Dictionary (ซ้อนกันหลายชั้น)

# คุณได้รับข้อมูลสภาพอากาศ (Weather Data) และต้องการดึงเฉพาะ "อุณหภูมิ (temp)" และ "เมือง (city)" ออกมา
weather_api = {
  "status": "success",
  "data": {
    "location": {
      "city": "Bangkok",
      "country": "TH"
    },
    "current": {
      "temp_c": 32.5,
      "humidity": 60,
      "condition": "Sunny"
    }
  }
}
# โจทย์: จงเขียนโค้ดเพื่อดึงค่า city และ temp_c ออกมาแสดงผล
city = weather_api["data"]["location"]["city"]
temp_c = weather_api["data"]["current"]["temp_c"]
print(f"City: {city}, Temperature: {temp_c}°C")