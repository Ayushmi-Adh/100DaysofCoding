#NUMBER GUESSING GAME
from art import logo4
from random import randint
print(logo4)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

SET_EASY_LEVEL = 10
SET_HARD_LEVEL = 5
def choose_level():
    level = input("choose a difficulty level, Type 'easy' or'hard': ").lower()
    if level=="easy":
        return SET_EASY_LEVEL
    else:
        return SET_HARD_LEVEL
    
def check_number(guess_number,attempts,correct_number):
    if guess_number>correct_number:
        print("Too high.")
        return attempts-1
    elif guess_number<correct_number:
        print("Too low.")
        return attempts-1
    else:
        print(f"You guessed the number. The answer was {correct_number}")

def final_game():
    correct_number = randint(1,100)
    print(f"Pssst, the correct number is {correct_number}.")

    guess_number = 0
    attempts =choose_level()
    while not guess_number==correct_number:
        print(f"You have {attempts} attempts remaining.")
        guess_number=int(input("Make a guess: "))
        attempts=check_number(guess_number,attempts,correct_number)
        if attempts==0:
            print("You ran out of guesses.You loose!!!")
            return
        else:
            print("Guess again!")

final_game()







# def game():
#     global correct_number
#     global num
#     while num==True:
#         guessed_num = int(input("Make a guess: "))
#         if guessed_num>correct_number:
#             print("Too high")
#         elif guessed_num==correct_number:
#             print("You got it! The answer was 69.")
#             num=False
#         else:
#             print("Too low.")
#         num-=1
#         print(f"You have {num} attempts remaining to guess the number.")
# if level =="easy":
#     if num<=10 and num>=1:
#         num = True
#     print("You have 10 attempts remaining to guess the number.")
#     game()
#     print("You didn't guess the number.You loose!!")
# else:
#     num-=5
#     if num<=5 and num>=1:
#         num = True
#     print("You have 5 attempts remaining to guess the number.")
#     game()
#     print("You didn't guess the number.You loose!!")


