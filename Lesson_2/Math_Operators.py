# โจทย์: โรงงานผลิตน้ำดื่ม
total_bottles = 125  # มีน้ำทั้งหมด 125 ขวด
pack_size = 6        # 1 แพ็ค มี 6 ขวด

# 1. หารปกติ (Division) -> ได้ทศนิยม
raw_division = total_bottles / pack_size
print(f"หารปกติ: {raw_division}")

# 2. หารเอาจำนวนเต็ม (Floor Division) -> เพื่อดูว่าจะแพ็คได้กี่แพ็คเต็มๆ
total_packs = total_bottles // pack_size
print(f"จำนวนแพ็คที่ได้: {total_packs} แพ็ค")

# 3. หารเอาเศษ (Modulo) -> เหลือเศษกี่ขวดที่แพ็คไม่ได้ (ต้องคัดออกหรือรอรอบหน้า)
leftover = total_bottles % pack_size
print(f"เหลือเศษ: {leftover} ขวด")