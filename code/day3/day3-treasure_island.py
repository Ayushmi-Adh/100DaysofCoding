#TREASURE ISLAND
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************

''')

print("  ***WELCOME TO THE TREASURE ISLAND***  ")
print("---Your mission is to find the treasure---")

choice_1 = input("Do you want to go to left or right?: ").lower()

if(choice_1=="left"):
    choice_2 = input("Do you want to swim or do you want to wait?: ").lower()
    if(choice_2=="wait"):
        choice_3 = input("Choose a color of the door you would like to go inside:(red/blue/yellow): ").lower()
        if(choice_3=="yellow"):
            print("You found the treasure. YOU WIN!!")
        else:
            print("The darkness have found you.GAME OVER!")
    else:
        print("You got eaten by a crocodile.Game Over!!!")
else:
    print("You fell into the hole. Game Over!!!")