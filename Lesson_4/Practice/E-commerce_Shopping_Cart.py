branch_a = ["Bob", "Alice"]
branch_b = ["Charlie", "Eve", "David"]

# รวมรายชื่อลูกค้าทั้งสองสาขา
all_customers = branch_a + branch_b
print(f"รายชื่อลูกค้าทั้งหมด: {all_customers}")

# เรียงลำดับรายชื่อลูกค้า A-Z
all_customers.sort()
print(f"รายชื่อลูกค้าเรียง A-Z: {all_customers}")

# นับจำนวนลูกค้าทั้งหมด
total_customers = len(all_customers)
print(f"จำนวนลูกค้าทั้งหมด: {total_customers}")