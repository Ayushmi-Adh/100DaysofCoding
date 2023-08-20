#ROCK PAPER SCISSOR
import random
rock =  '''
        ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
    '''
              
paper = '''
            ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'       
'''

scissor = ''' 
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
  '''

game_image = [rock,paper,scissor]
our_choice = int(input("Enter 0 for rock, 1 for paper and 2 for scissor: "))

print(game_image[our_choice])
random_choice = random.randint(0,2)
print("Computer chose:")
print(game_image[random_choice])


if our_choice>=3 or our_choice<0:
    print("You typed an invalid number, you lose!") 

elif our_choice==0 and random_choice==2:
    print("You win!!!")

elif random_choice==0 and our_choice==2:
    print("You lose!!!")

elif(random_choice>our_choice):
    print("You lose!!!")

elif(our_choice>random_choice):
    print("You win!!!")

elif (random_choice==our_choice):
    print("\nDraw!!!")





