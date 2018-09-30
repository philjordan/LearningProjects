'''
Created on Sep 22, 2018

@author: Phil
'''
import random

answer = str(random.randint(1,100))
tries = 1
guess = input("Guess a number 1-100: ")
while guess != answer:
    #print(answer)
    if guess > answer:
        tries=tries+1
        guess = input("To high, pick again: ")
    else:
        tries=tries+1
        guess = input("To low, pick again: ")
print ("It took you " + str(tries) + " tries but you got it right!")
