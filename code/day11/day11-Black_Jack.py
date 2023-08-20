#BlackJack
import random

def deal_card():
    cards_available = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards_available)

def calculate(cards_available):
    if sum(cards_available)==21 and len(cards_available)==2:
        return 0
    
    if 11 in cards_available  and sum(cards_available)>21:
        cards_available.remove(11)
        cards_available.append(1)
        
    return sum(cards_available)

User_choice = []
Computer_choice = []

for _ in range(2):
    User_choice.append(deal_card())
    Computer_choice.append(deal_card())

user_total_Score = calculate(User_choice)
computer_score = calculate(Computer_choice)

if User_choice ==0 or Computer_choice ==0 or user_total_Score>21:
    is_game_over = True
else:
    more_card = input("Type 'yes' to get another card and 'no'tp pass: ").lower()
    if more_card =="yes":
        User_choice.append(deal_card())
    else:
        is_game_over = True
