#CAESAR-CIPHER
from art import logo
print(logo)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(plain_text,shift_number,cipher_direction):
        cipher_text = ""
        if cipher_direction =="decode":
            shift_number *= -1
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_number
                cipher_text += alphabet[new_position]
            else:
                 cipher_text += letter
        print(f"The {cipher_direction}d text is:{cipher_text}")

continue_ = True
while continue_:
    direction = input("Type 'encode' to encrypt, type 'decode; to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int (input ("Type the shift number: "))
    shift = shift % 26
    
    caesar(plain_text=text, shift_number=shift, cipher_direction=direction)

    ask = input("Type 'yes' if you want to go again.Otherwise type 'no':").lower()

    if ask=="no":
        continue_ = False
        print("GoodBye!")
     