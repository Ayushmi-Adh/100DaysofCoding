#HIGHER LOWER GAME
import random
import os
from art import logo5,logo6
from gamedataforday12 import data
print(logo5)

def get_account():
  """Get data from random account"""
  return random.choice(data)

def choose_and_display(random_account):
  name =random_account["name"]
  description = random_account["description"]
  country = random_account["country"]

  return f"{name}, a {description}, from {country}" 


def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
  
def game():
  should_continue = True
  account_a = get_account()
  account_b = get_account()
  score=0
  while should_continue:
    account_a = account_b
    account_b = get_account()
    
    while account_a==account_b:
      account_b = get_account()

    print(f"Compare A:{choose_and_display(account_a)}")
    print(logo6)
    print(f"Against B:{choose_and_display(account_b)}")

    guess = input("Who has more instagram followers, Type 'A' or 'B': ").lower()

    a_count = account_a["follower_count"]
    b_count = account_b["follower_count"]
    to_check = check_answer(guess,a_count,b_count)

    os.system('cls')
    print(logo5)
    if to_check:
      score +=1
      print(f"You are right! Current score:{score}")
    else:
      should_continue=False
      print(f"Sorry, that is wrong. Final score is {score}")

game()


























































# def display_option():
#     if option=="name" or option=="description" or option=="country":
#         if option =="description":
#             print("a",value, end=",")
#         elif option =="country":
#             print("from",value)
#         elif option!="description" and option!="country":
#             print(value,end=",")
    
   

# for option in range(get_account(),2):
#     value = [option]
#     display_option()
    



