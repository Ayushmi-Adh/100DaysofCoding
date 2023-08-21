# -100daysofcoding-
Welcome to my 100 Days of Coding Python challenge! This is a personal coding journey where I'll be coding and learning Python for the next 100 days. Follow along to see my progress and the projects I'll be working on.
 
![68747470733a2f2f7334313636302e7063646e2e636f2f77702d636f6e74656e742f75706c6f6164732f323032302f30342f39302d61727469636c652d62616e6e65722d322e676966](https://github.com/Ayushmi-Adh/100DaysofCoding/assets/132826306/bc5e6226-bb96-4033-8e26-cc7bf1e6d583)


## Table of Contents
- [About the Challenge](#about-the-challenge)
- [My Goals](#my-goals)

## Basic Level Python Projects
|S.N|    Projects    | 
|---|----------------|
| 1 | [Coffee Machine](/code/day15/CoffeeMachine.py)   | 
| 2 | [Rock,Paper,Scissor](/code/day4/day4-rock_paper_scissor.py) |
| 3 | [HangMan Game](/code/day6/hangmanGame.py)|
| 4 | [Ceasar Cipher](/code/day8/day8-ceaesar-cipher.py)|
| 5 | [Blind Auction](/code/day9/day9-blind-auction.py)|
| 6 | [Black-Jack](/code/day11/day11-Black_Jack.py)|



## About the Challenge

The 100 Days of Coding Python challenge is an initiative to consistently work on coding projects and improve Python skills. The challenge involves dedicating at least an hour every day to coding, learning, and building various Python projects.

## My Goals

- Improve my Python programming skills.
- Gain hands-on experience in building real-world projects.
- Learn and apply different Python libraries and frameworks.
- Develop problem-solving and algorithmic thinking abilities.

# Day-1
## Band Name Generator

This is a simple Python program that generates band names using the name of your city and your pet's name.

**How It Works**

1. The program will prompt you to enter the name of your city.
2. Then, it will ask you to provide your pet's name.
3. The program will combine the two names to create a unique band name.

![image](https://github.com/Ayushmi-Adh/100DaysofCoding/assets/132826306/165cab1f-d138-49ac-b210-4dcf710aaddd)


## Breakdown of Basic Python concepts used in Day-1
 The "Band Name Generator" program is a simple example that uses some basic concepts of Python programming. 

1. **Input and Output:**
   The program uses the `input()` function to prompt the user for input. It then uses the `print()` function to display the generated band name.

2. **Variables:**
   The program uses variables to store the user's input (`name` and `name2`) and the combined band name (`band_name`).

3. **String Concatenation:**
   String concatenation is used to combine the user's input for the city name and pet's name to create the band name. The `+` operator is used to concatenate strings.

4. **Control Flow:**
   The program follows a linear sequence of steps, where each step prompts the user for input and then proceeds to the next step. There are no explicit conditional statements or loops in this program.

5. **Function Calls:**
   The program uses the `input()` and `print()` functions, which are built-in Python functions, to interact with the user and display output.

# Day-2
## Tip Calculator

This is a simple Python program that calculates the total bill per person, including the tip, based on the total bill amount, tip percentage, and the number of people sharing the bill.

**How It Works**

1. The program will prompt you to enter the total bill amount.
2. Then, it will ask you to provide the tip percentage you want to give (10, 12, or 15).
3. Next, it will prompt you to specify the number of people sharing the bill.
4. The program will calculate the tip amount, add it to the total bill, and then divide the total among the specified number of people.
5. It will display the amount each person needs to pay.

   ![image](https://github.com/Ayushmi-Adh/100DaysofCoding/assets/132826306/52a976c0-6c25-4d1a-a184-0df39b60f46c)


   **"print(f"Each person should pay ${round(each_person, 2)}")"**
   
-In this line of code, the `print()` function uses an `f-string` to create a formatted string that displays the calculated amount each person should pay. Here's the breakdown of how it works:

1.f"...": The f before the string indicates that it's an `f-string`.

2.{round(each_person, 2)}: The expression within the curly braces is evaluated and replaced with the rounded value of each_person with 2 deci mal places.

# Day-3
## Treasure Island Adventure

Experience an interactive text-based adventure in the "Treasure Island" game. Your mission is to find the hidden treasure! Follow the clues, make choices, and see if you can successfully discover the treasure.

**How It Works**

1. You are presented with a textual representation of the island.
2. You are given choices at each stage of the story.
3. Based on your choices, the story progresses and may lead you to success or failure.

   ![image](https://github.com/Ayushmi-Adh/100DaysofCoding/assets/132826306/83af87c2-33bb-42af-a60c-ff6f7055d1fb)


# Day-4
## Rock Paper Scissors Game

Play the classic game of Rock Paper Scissors against the computer. Make your choice and see if you can beat the computer's selection!

**How It Works**

1. You choose between rock, paper, and scissors by entering the respective numbers (0 for rock, 1 for paper, and 2 for scissors).
2. The computer randomly selects one of the options.
3. The game evaluates the choices and determines the winner or if it's a draw.

![image](https://github.com/Ayushmi-Adh/100DaysofCoding/assets/132826306/48080c42-cc73-4aa4-b5e7-026438acb728)


## ASCII ART
-"Treasure Island," "Rock Paper Scissors," and "Band Name Generator" programs, I've used ASCII art to enhance the user experience and add a visual element to the text-based programs. This can make our programs more engaging and visually appealing, especially when shared with others.


# Day-5
## PyPassword Generator

Generate secure and randomized passwords with the "PyPassword Generator" program. This program creates passwords based on your desired number of letters, symbols, and numbers.

 **How It Works**

1. The program prompts you to specify the number of letters, symbols, and numbers you want in your password.
2. It randomly selects characters from alphabets, symbols, and numbers to create a password.
3. The password is shuffled to ensure randomness.
4. The final password is displayed to you.

   ![image](https://github.com/Ayushmi-Adh/100DaysofCoding/assets/132826306/85602430-5ca2-4b60-a7ea-500cb536e20b)


# Lists and Importing Modules in Python

In Python, lists are a fundamental data structure that allow you to store and manipulate collections of items. Lists can contain elements of different types, including integers, strings, and more. They are useful for tasks like storing multiple values, iterating over elements, and dynamically managing data.

Python also provides the ability to import modules, which are collections of related functions, classes, and variables. Modules allow you to organize your code into reusable components and access functionality beyond the built-in features of the Python language.

**Lists**

Lists are defined using square brackets `[]`, and elements are separated by commas. They support indexing (starting from 0) and slicing to access specific elements or portions of the list. Lists can be modified, resized, and extended using various methods.

Example of creating a list:
```python
my_list = [1, 2, 3, "aayushmi", True]
```
# Day-7
## HangMan Game

Play the classic game of Hangman and guess the secret word before you run out of lives. Have fun testing your vocabulary and logic skills!

**How It Works**

1. The game randomly selects a secret word from a predefined list
2. You have a limited number of lives to guess the letters in the word.
3. For each correct guess, the letter is revealed in its correct position.
4. For each incorrect guess, you lose a life and part of the hangman drawing is displayed.
5. Your goal is to guess the entire word before running out of lives.

<img width="252" alt="image" src="https://github.com/Ayushmi-Adh/100DaysofCoding/assets/132826306/2bdfbcbf-35cf-4fb1-8da9-58347fd360e3">





