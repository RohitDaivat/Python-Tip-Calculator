print("Welcome to the python restaurant tip calculator.")

#input the value
total_bill = input("what was the total bill? $")
total_bill = float(total_bill)

percent_tip = input("What Percentage tip would you like to give? 5, 10 or 15? ")
percent_tip = int(percent_tip)

total_ppl = input("Enter the Number of people to split the bill? ")
total_ppl = int(total_ppl)

#calculations

total_percent = (percent_tip / 100) * total_bill
total_percentbill = total_percent + total_bill

split_bill = total_percentbill / total_ppl
split_bill = round(split_bill, 2)

formatted_bill = f"{split_bill:.2f}"

print(f"Each person should pay ${formatted_bill}")


