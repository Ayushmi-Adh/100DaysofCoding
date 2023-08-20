#Pizza Delivery Service

print("WELCOME TO THE PYTHON PIZZA DELIVERIES!!")
size = input("What size pizza do you want?S,M,L: ").upper()
add_pepperoni = input("Do you want pepperoni? Type Y for yes and N for no: ").upper()
extra_cheese = input("Do you want extra cheese? Press Y for yes and N for no: ").upper()

if(size=="S"):
    bill_1=15
    if(add_pepperoni=="Y"):
        bill_1=15+2
elif(size=="M"):
    bill_1=20
    if(add_pepperoni=="Y"):
        bill_1=20+3
else:
    bill_1=25
    if(add_pepperoni=="Y"):
        bill_1=20+3

if(extra_cheese=="Y"):
    bill_2=1
else:
    bill_2=0

total_bill = bill_1+bill_2

print(f"Your final bill is: ${total_bill}.")


