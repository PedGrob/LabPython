prices = [3.5, 2.0, 9.0, 4.5, 3.0]
# เรียงลำดับราคาจากน้อยไปมาก
prices.sort()
print(f"ราคาที่เรียงลำดับ: {prices}")

# หาข้อมูลตำแหน่งกลาง (Median)
length = len(prices)
if length % 2 == 1:
    median_price = prices[length // 2]
else:
    mid1 = prices[(length // 2) - 1]
    mid2 = prices[length // 2]
    median_price = (mid1 + mid2) / 2
print(f"ราคากลาง (Median): {median_price}")

# Report
print(f"ข้อมูลแบบเรียงลำดับ: {prices}")
print(f"Median Price: {median_price} ล้านบาท")