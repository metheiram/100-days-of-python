print("Welcome to the tip calculator")
total=float(input("what was the total bill $ "))
tip=int(input("how much tip would you like to give? 10,12,15?"))
people=int(input("how many people to split  the bill "))

bill_with_tip = tip/100 * total + total
bill_per_person = bill_with_tip/people
final_amount = round(bill_per_person , 2)
print(f"each person sould pay ${final_amount} ")