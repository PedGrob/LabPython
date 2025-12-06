# Input
Input_usd = float(input("Enter amount in USD: ")) # รับจำนวนเงินดอลลาร์สหรัฐ
Input_exchange_rate = float(input("Enter exchange rate (1 USD to THB): ")) # รับอัตราแลกเปลี่ยน

# Calculations
Amount_thb = Input_usd * Input_exchange_rate # คำนวณจำนวนเงิน

# Print Result
# print(f"\nAmount USD: {Input_usd:,.2f} USD")
# print(f"Exchange Rate (THB/USD): {Input_exchange_rate:,.2f} THB/USD")
# print(f"USD Amount: ${Input_usd:,.2f} USD")
# print(f"Exchange Rate: {Input_exchange_rate:,.2f} THB/USD")
# print(f"THB Amount: {Amount_thb:,.2f} THB")

print(f"""
Amount in USD:         {Input_usd:>12,.2f} USD
Exchange Rate (THB/USD): {Input_exchange_rate:10,.2f} THB/USD
Amount in THB:         {Amount_thb:>12,.2f} THB
""")