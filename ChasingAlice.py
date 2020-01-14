#Amritpal Saini, 30039983, Catalin Dohotaru, Section 2

import turtle # Allows the use of turtle functions
from random import randint #allows the use of randint, which returns a random integer, from the random catalog

def WinSetup(): #Short for Window Setup, function is used to create the window
    wn = turtle.Screen()
    wn.setup(500, 500)
    return

def TurtleToRandomSpot(Turtle): #Function is used to move a given turtle to a random location
    Turtle.up()
    x = randint(-249, 249)
    y = randint(-249, 249)
    Turtle.setpos(x, y)
    Turtle.down()
    return

def AlexSetup():  # This function is used to setup the turtle moved by the player
    Alex = turtle.Turtle(shape='turtle') #Names the turtle and gives the turtle a turtle shape
    Alex.color("blue") #Different color to tell the difference
    Alex.setpos(0, 0)
    # Alex must always start in the center
    return Alex

def AliceSetup(): #This function is to setup the computer controlled turtle
    #Same as AlexSetup but Alice starts in a random location
    Alice = turtle.Turtle(shape="turtle")
    Alice.color("red")
    TurtleToRandomSpot(Alice)
    return Alice

def AliceMove(Alice): #This function moves the computer controlled turtle
    MakeMove = randint(1,6) #MakeMove is assigned a random integer from 1 to 6, including 1 and 6.
    if MakeMove == 1: #1/6 of the time, Alice will turn right
        Alice.right(90)
    elif MakeMove == 2: #1/6 of the time, Alice will turn right
        Alice.left(90)
    else:
        Alice.forward(20) #2/3 of the time, Alice will go straight
    #1/3 of the time, Alice turns, 2/3 of the time, Alice moves straight
    return

def AlexMove(Alex):  # This is the function to control the movement of Alex
        GiveMove = input("Move Alex: ") #GiveMove is asking the user for an input
        if (GiveMove == 'w'):
            Alex.forward(30)
            return True
        elif (GiveMove == 's'):
            Alex.backward(30)
            return True
        elif (GiveMove == 'a'):
            Alex.left(45)
            return True
        elif (GiveMove == 'd'):
            Alex.right(45)
            return True
        else:
            print(GiveMove, "is not recognized as a movement. Retype") #Error message if w,s,a,d was not entered
            return False

def MovementAndWriter(Alex, Alice): #controls when the turtles should move and ends the game
    counter = 0 #required for steps in writing
    Writer = turtle.Turtle() #turtle specific for writing
    Writer.ht()
    Writer.up()
    Writer.goto(-230, 230) #goes to the top left corner
    Writer.down()
    while (Alex.distance(Alice) > 30): #main movement loop. While Alice isn't caught, keep playing
        Distance = str(round(Alex.distance(Alice), 2)) #used for writing distance
        #was unsure of how to round, https://stackoverflow.com/questions/20457038/python-how-to-round-down-to-2-decimals
        if AlexMove(Alex): #only move Alice if alex actually moves
            AliceMove(Alice)
            counter += 1 #increment for steps in writing
            Writer.clear() #clear the pervious writing, if any
            Writer.write("Step# " + str(counter) + " Distance between Alex & Alice: " + Distance, False,
                         align="left",
                         font=("Ariel", 12, "normal"))
            #the actual writing at the top
        cond1 = Alex.distance(0,0) >= 250
        cond2 = Alice.distance(0, 0) >= 250
        #https://stackoverflow.com/questions/181530/styling-multi-line-conditions-in-if-statements
        #cond1 and cond2 are conditions for controlling the border.
        if Alex.distance(Alice) < 30: #If alice is caught
            NewDis = str(round(Alex.distance(Alice), 2)) #update distance
            Writer.clear() #clear previous writing
            Writer.write("Step# " + str(counter) + " Distance between Alex & Alice: " + NewDis, False,
                         align="left",
                         font=("Ariel", 12, "normal"))
            #write new distance and step
            turtle.mainloop() #end the game
        elif cond1: #if Alex steps out of the game, return to random spot
            TurtleToRandomSpot(Alex)
        elif cond2: #if alice steps out of the game, return to random spot
            TurtleToRandomSpot(Alice)

def main(): #used to run all functions and
    WinSetup()
    Alex = AlexSetup()
    Alice = AliceSetup()
    MovementAndWriter(Alex, Alice)

main()


