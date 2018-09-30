'''
Created on Sep 22, 2018

@author: Phil
'''
import random
from _tracemalloc import stop
playTheGame = input ("Would you like to roll the dice? Y or N: ")
playTheGame = playTheGame.lower()
while playTheGame != "n":
    if playTheGame != "y":
        print("Invalid Entry")
        playTheGame = input ("Would you like to roll the dice? Y or N: ")
    else:
        roll = str(random.randint(1,6))
        print ("You rolled a " + roll + ".")
        playTheGame = input("Would you like to roll again? Y or N: ")
        playTheGame = playTheGame.lower()
print("Goodbye")