'''
Created on Sep 29, 2018

@author: Phil

Text game to move around.  3x3 grid with user starting at bottom left.  Each move will adjust the x,y axis.
Need to define the rooms and prompt the user to make a move.

                    N
    family room    dining room    kitchen
W   game room      lounge         butlers pantry   E
    study          main hall      sitting room
                   exit 
                     S   
wall between study and game room.  Wall between lounge and butlers pantry.  can't go outside the box with the exception of the exit.
'''
from unicodedata import bidirectional
x_cord=0
y_cord=1


room01description = "You have entered the main hall.  To the north of you is the lounge, to the east the sitting room, to the west the study.  To your south is the exit."
room00description = "You have entered the study.  To your east is the main hall."
room02description = "You have entered the sitting room.  To your west is the main hall, to the north is the butlers pantry."
room10description = "You have entered the game room.  To your north is the family room, to your east is the lounge."
room20description = "You have entered the family room.  To the south is the game room, to the east is the dining room."
room21description = "You have entered the dining room.  To the south is the lounge, to the west the family room and to the east the kitchen."
room22description = "You have entered the kitchen.  To the south is the butlers pantry, to the west is the dining room."
room11description = "You have entered the lounge.  To the north is the dining room, to the west is the game room, to the south is the main hall."
room12description = "You have entered the butlers pantry.  To the north is the kitchen, to the south the sitting room."
    
#Function to print the room description of where you are currently
def roomlocation (x_cord, y_cord):
    if x_cord==0 and y_cord==0:
        print(room00description)
    elif x_cord==0 and y_cord==1:
        print(room01description) 
    elif x_cord==0 and y_cord==2:
        print(room02description)
    elif x_cord==1 and y_cord==0:
        print(room10description)
    elif x_cord==1 and y_cord==1:
        print(room11description)
    elif x_cord==1 and y_cord==2:
        print(room12description)
    elif x_cord==2 and y_cord==0:
        print(room20description)
    elif x_cord==2 and y_cord==1:
        print(room21description)
    elif x_cord==2 and y_cord==2:
        print(room22description)
    else:
        print("We shouldn't be here")

#function to update the x and y coordinates based on where you selected to move
def move (direction, x_cord, y_cord):
    if x_cord == 0 and y_cord == 1 and direction == 'S':
        while True:
            message = input("You have exited the house.  Are you sure you want to leave? Y/N ")
            if message == "Y":
                exit()
            elif message =="N":
                return (x_cord, y_cord)
                break
            else:
                continue
    elif direction == 'N':
        if x_cord == 2:
            print("You ran into a wall.")
        else:
            x_cord = x_cord+1
            y_cord = y_cord
        return (x_cord, y_cord)
    elif direction == 'E':
        if y_cord == 2:
            print("You ran into a wall.")
        else:
            x_cord = x_cord
            y_cord += 1
        return (x_cord, y_cord)
    elif direction == 'S':
        if x_cord == 0:
            print("You ran into a wall.")
        else:
            x_cord -=1
            y_cord = y_cord
        return (x_cord, y_cord)
    else:
        if y_cord == 0:
            print("You ran into a wall.")
        else:
            x_cord = x_cord
            y_cord -=1
        return (x_cord, y_cord)
        

while x_cord>=0: 
    roomlocation(x_cord, y_cord)
    direction = input("Where would you like to go? ")
    x_cord,y_cord = move(direction, x_cord, y_cord)



'''
#need to find a way to exit when the coordinates are 0,-1
leave = 'N'
while leave != 'N':
    message = 'N'
    if x_cord == -1 and y_cord == 1:
        while message != "N":
            message = input("You have exited the house.  Are you sure you want to leave? Y/N ")
            if message == 'Y':
                print("Goodbye!")
                exit()
            elif message == "N":
                x_cord += 1
                print(x_cord)
                print(y_cord)
            else:
                print("Invalid Entry.  Try again.")
                message = 'Y'
'''
