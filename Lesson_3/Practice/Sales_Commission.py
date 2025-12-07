# Input
sales_amount = int(input("Enter Sales Amount: "))

# Logic to determine sales commission
if sales_amount > 50000:
    commission = "10%"
    total = sales_amount * 0.10
elif sales_amount > 20000:
    commission = "5%"
    total = sales_amount * 0.05
else:
    commission = "0%"
    total = sales_amount * 0.00


# Output
print(f"ได้ค่าคอมมิชชั่น {commission} เป็นจำนวนเงิน {total} บาท")