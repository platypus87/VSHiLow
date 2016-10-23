"""Plays a Hi/Low game with user-entered range
and keeps track of the number of guesses (without methods)"""

import random
range=int(input("Please enter the maximum number of the range you would like to guess within: "))
gennum = random.randrange(range+1)
guess = int(input("Please enter a number within the range: "))
counter =1

print("The computer-generated number is: ",gennum)

if guess==gennum:
    print("Congrats, you guessed right on the first try!")

while not guess==gennum:
    if guess>gennum:
        print(guess,"is too high, please try again: ")
        guess = int(input("Please enter a number within the range: "))
        counter+=1
    elif guess<gennum:
        print(guess,"is too low, please try again: ")
        guess = int(input("Please enter a number within the range: "))
        counter+=1

print("It took you",counter,"guesses to guess correctly.")