#PyPassword Generator:
import random
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!','.','-','_','@','#','$','%','&','*']
numbers = ['1','2','3','4','5','6','7','8','9','0']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols= int(input("How many symbols would you like?\n"))
nr_numbers= int(input("How many numbers would you like?\n"))
password =[]
for char in range(1,nr_letters+1):
    password += random.choice(alphabet)

for char in range(1,nr_symbols+1):
    password += random.choice(symbols)

for char in range(1,nr_numbers+1):
    password += random.choice(numbers)

print(password)
random.shuffle(password)
print(password)

passWord =""
for char in password:
    passWord+= char

print(f"Your password is:{passWord}")
