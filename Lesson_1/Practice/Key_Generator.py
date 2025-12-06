#Input
input_catagory = input("Enter category (เช่น อาหาร, เครื่องดื่ม): ")
input_product_id = input("Enter product ID (รหัสตัวเลขสินค้า): ")
input_year = input("Enter year of production (ปีที่ผลิต): ")
#Generate Key
product_key = f"{input_catagory}-{input_product_id}-{input_year}"
#Output
print("\n--- Product Key Generated ---")
print(f"Category Code: {input_catagory}")
print(f"Product ID: {input_product_id}")
print(f"Production Year: {input_year}")
print(f"Generated SKU: {product_key}")