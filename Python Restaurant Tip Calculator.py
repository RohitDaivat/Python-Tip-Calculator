print("Welcome to the Python Restaurant tip calculator.")
total_bill = input("what was the total bill? $")
total_bill = float(total_bill)

percent_tip = input("What Percentage tip would you like to give? 10, 12 or 15? ")
percent_tip = int(percent_tip)

total_ppl = input("how many people to split the bill? ")
total_ppl = int(total_ppl)

# calculation wala part

total_percent = (percent_tip / 100) * total_bill
total_percentbill = total_percent + total_bill

split_bill = total_percentbill / total_ppl

print(f"Each person should pay ${split_bill}")
