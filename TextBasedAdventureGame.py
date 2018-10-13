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

add random insults

add the ability to pick up and drop items

make the goal to make pancakes
'''
from unicodedata import bidirectional
x_cord=0
y_cord=1

wall="You ran into a wall."

studyItems = ["hat", "coat", "milk"]
mainHallItems= ['cat', 'phone', 'baking soda']
sittingRoomItems=['empty wine glass', 'eggs']
gameRoomItems=['skillet', 'poker chips']
lougeItems=['butter', 'fedora']
butlersPantryItems = ['flour', 'thin mints']
familyRoomItems = ['remote control', 'salt' ]
dingingRoomItems = ['sugar', 'chair']
kitchenItems = ['wine']
myItems = []


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
def go (direction, x_cord, y_cord):
    if x_cord == 0 and y_cord == 1 and direction == 's':
        while True:
            message = input("You have exited the house.  Are you sure you want to leave? Y/N ")
            message = message.lower()
            if message == "y":
                exit()
            elif message =="n":
                return (x_cord, y_cord)
                break
            else:
                continue
    elif direction == 'n':
        if x_cord == 2:
            print(wall)
        else:
            x_cord = x_cord+1
        return (x_cord, y_cord)
    elif direction == 'e':
        if y_cord == 2:
            print(wall)
        else:
            y_cord += 1
        return (x_cord, y_cord)
    elif direction == 's':
        if x_cord == 0:
            print(wall)
        else:
            x_cord -=1
        return (x_cord, y_cord)
    else:
        if y_cord == 0:
            print(wall)
        else:
            y_cord -=1
        return (x_cord, y_cord)
       
#function to look around the room and find what is there
def look (x_cord, y_cord):
    if x_cord==0 and y_cord==0:
        return (", ".join(studyItems))
    elif x_cord==0 and y_cord==1:
        return(", ".join(mainHallItems))
    elif x_cord==0 and y_cord==2:
        return(", ".join(sittingRoomItems))
    elif x_cord==1 and y_cord==0:
        return(", ".join(gameRoomItems))
    elif x_cord==1 and y_cord==1:
        return(", ".join(lougeItems))
    elif x_cord==1 and y_cord==2:
        return(", ".join(butlersPantryItems))
    elif x_cord==2 and y_cord==0:
        return(", ".join(familyRoomItems))
    elif x_cord==2 and y_cord==1:
        return(", ".join(dingingRoomItems))
    else:
        return(", ".join(kitchenItems))

def drop (item, x_cord, y_cord):
    myItems.remove(item)
    if x_cord==0 and y_cord==0:
        studyItems.append(item)
    elif x_cord==0 and y_cord==1:
        mainHallItems.append(item)
    elif x_cord==0 and y_cord==2:
        sittingRoomItems.append(item)
    elif x_cord==1 and y_cord==0:
        gameRoomItems.append(item)
    elif x_cord==1 and y_cord==1:
        lougeItems.append(item)
    elif x_cord==1 and y_cord==2:
        butlersPantryItems.append(item)
    elif x_cord==2 and y_cord==0:
        familyRoomItems.append(item)
    elif x_cord==2 and y_cord==1:
        dingingRoomItems.append(item)
    else:
        kitchenItems.append(item)

def pickup (item, x_cord, y_cord):
    myItems.append(item)
    if x_cord==0 and y_cord==0:
        studyItems.remove(item)
    elif x_cord==0 and y_cord==1:
        mainHallItems.remove(item)
    elif x_cord==0 and y_cord==2:
        sittingRoomItems.remove(item)
    elif x_cord==1 and y_cord==0:
        gameRoomItems.remove(item)
    elif x_cord==1 and y_cord==1:
        lougeItems.remove(item)
    elif x_cord==1 and y_cord==2:
        butlersPantryItems.remove(item)
    elif x_cord==2 and y_cord==0:
        familyRoomItems.remove(item)
    elif x_cord==2 and y_cord==1:
        dingingRoomItems.remove(item)
    else:
        kitchenItems.remove(item)

    
'''
#function to define what is in a room
def pickup (x_cord, y_cord):
    roomlocation(x_cord, y_cord)
    

#function to define what is on our person
#allowed to check inventor, add to it or drop something.  Max objects to hold is two
def holding (action):
'''   
actions=["go", "look", "pickup", "drop", "insult", "help"]
print('While walking down the road, you randomly decide to enter a small house you see.' '\n'
      'Enter "go" to move, "look" to see what is in each room,' '\n'
      '"pickup" to grab objects, "drop" to drop objects,' '\n'
      'and "help" to repeat these instructions.' '\n')
while x_cord>=0: 
    roomlocation(x_cord, y_cord)
    while True:
        action = input("What would you like to do? ")
        action = action.lower()
        if action in actions:
            if action == "go":
                direction = input("Where would you like to go? (N, S, E, or W)")
                direction=direction.lower()
                valid_direction = {'n', 's', 'e', 'w'}
                if direction in valid_direction:
                    break
                else:
                    continue
            elif action == "look":
                    items = look(x_cord,y_cord)
                    print("The room contains: " + items)
            elif action == "pickup":
                    topickup = input("What would you like to pickup? ")
                    topickup = topickup.lower()
                    if topickup in look(x_cord, y_cord):
                        #myItems.append(topickup)
                        pickup(topickup, x_cord, y_cord)
                        print("My items are:")
                        print(*myItems, sep = ", ")
                        print(look(x_cord, y_cord))
                        #drop(topickup,x_cord, y_cord)
                    else:
                        print("I don't see that in this room.")
            elif action == "drop":
                if len(myItems) == 0:
                        print("Your hands are empty")
                elif:
                    todrop = input("What would you like to drop? ")
                    todrop = todrop.lower()
                    if todrop in myItems:
                        drop(todrop, x_cord, y_cord)
                    else:
                        print("You aren't holding that item.")
                    #else:
                        #print(*myItems, sep = ", ")
            elif action == "help":
                print('Enter "go" to move, "look" to see what is in each room,' '\n'
                      '"pickup" to grab objects, "drop" to drop objects,' '\n'
                      'and "help" to repeat these instructions.' '\n')
        else:
            print ("Invalid entry.")
            continue
    x_cord,y_cord = go(direction, x_cord, y_cord)
