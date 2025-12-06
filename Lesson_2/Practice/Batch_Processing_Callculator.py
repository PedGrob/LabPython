# Input

print("=== ระบบคำนวณ Batch Processing ===")
total_records = int(input("กรุณาใส่จำนวนเรคคอร์ดทั้งหมดที่ต้องการประมวลผล: "))
batch_size = int(input("กรุณาใส่ขนาดของแต่ละ Batch (จำนวนเรคคอร์ดต่อ Batch): "))

# Calculate number of full batches
full_batches = total_records // batch_size
print(full_batches)
# Calculate leftover records that don't fit into a full batch
leftover_records = total_records % batch_size
print(leftover_records)
# Determine if there are any leftover records
has_leftover = leftover_records > 0
print(has_leftover)
# Total batches needed (including an extra batch for leftovers if any)
total_batches = full_batches + (1 if has_leftover else 0)
print(total_batches)
# Print results
print("\n--- ผลการคำนวณ Batch Processing ---")
print(f"จำนวนเรคคอร์ดทั้งหมด: {total_records}")
print(f"ขนาดของแต่ละ Batch: {batch_size}")
print(f"จำนวน Batch ที่ต้องใช้: {total_batches}")