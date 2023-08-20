#LOVE CALCULATOR

your_name = (input("Enter your name:")).lower()
lover_name = input("Enter your lover's name:").lower()

concat_names = your_name+lover_name

count_t = concat_names.count("t") + concat_names.count("r") + concat_names.count("u") + concat_names.count("e")
count_l = concat_names.count("l") + concat_names.count("o") + concat_names.count("v") + concat_names.count("e")
total_percent = str(count_t)+str(count_l)

total = int(total_percent)

if (total < 10 or total >90):
    print(f"Your score is {total}%, you go together like coke and mentos")
elif(total>40 and total<50):
    print(f"Your score is {total}%, you are alright together.")
else:
    print(f"Your score is {total}%")
    