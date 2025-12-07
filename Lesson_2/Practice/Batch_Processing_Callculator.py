# Input
print("=== ระบบคำนวณ Batch Processing ===")
total_records = int(input("กรุณาใส่จำนวนเรคคอร์ดทั้งหมดที่ต้องการประมวลผล: "))
batch_size = int(input("กรุณาใส่ขนาดของแต่ละ Batch (จำนวนเรคคอร์ดต่อ Batch): "))

# Calculate number of full batches
full_batches = total_records // batch_size # ใส่ได้เต็มกล่องกี่รอบ
print(full_batches)
# Calculate leftover records that don't fit into a full batch
leftover_records = total_records % batch_size # เหลือเรคคอร์ดที่ไม่พอใส่กล่องเท่าไหร่
print(leftover_records)

# Print results
print("\n--- ผลการคำนวณ Batch Processing ---")
print(f"จำนวนเรคคอร์ดทั้งหมด: {total_records}")
print(f"ขนาดของแต่ละ Batch: {batch_size}")
print(f"Full Batches: {full_batches} Rounds")
print(f"Remaining Records: {leftover_records} Records")