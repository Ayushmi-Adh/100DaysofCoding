#TIP CALCULATOR
print("WELCOME TO THE TIP CALCULATOR")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip you want to give (10, 12, or 15)? "))
bill_split = int(input("How many people to split the bill? "))

tip_amount = (tip/100)*total_bill
tip_plus_bill = total_bill + tip_amount
each_person = tip_plus_bill/bill_split

print(f"Each person should pay ${round(each_person,2)}")
