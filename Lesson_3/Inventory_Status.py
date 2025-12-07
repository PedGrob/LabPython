# โจทย์: คุณกำลังทำ Dashboard บริหารสต็อกสินค้า ให้เขียนโปรแกรมรับค่าจำนวนสินค้า (quantity) แล้วแสดงสถานะ:

# ถ้าสินค้าเหลือ 0 -> ให้แสดงว่า "Out of Stock"
# ถ้าสินค้าเหลือมากกว่า 0 -> ให้แสดงว่า "In Stock"

# Input
quantity = int(input("Enter the quantity of the item:"))

# Logic to determine inventory status
if quantity == 0:
    status = "Out of Stock"
elif quantity < 0:
    status = "Invalid Quantity"
else:
    status = "In Stock"

# Output
print("Inventory Status:", status)