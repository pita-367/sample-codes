#Pushpita Rahman
#Marina DiGregorio
#CS 172-062
#Lab 7

from room import *
from maze import *
import sys

# PATHWAY ANS:
# south --> east --> east --> east --> east --> east --> north --> north

#DEAD END PATHWAY
# north --> east --> north --> east --> north --> east 

##---OUR CODE HERE---

my_room = []
my_room.append(Room("This room is the entrance."))
my_room.append(Room("This room has a table. Maybe a dinning room?"))
my_room.append(Room("This room has blue walls. It's quite calming."))
my_room.append(Room("This room has a bed. Maybe a bedroom?"))
my_room.append(Room("This room has a parrot."))
my_room.append(Room("This room has a pool table"))
my_room.append(Room("This room has a reclining sofas"))
my_room.append(Room("This room has a shoestand and coat hanger"))
my_room.append(Room("This room is the exit. Good Job."))#8

#rooms to dead end
my_room.append(Room("This room has a television. Maybe a living room?"))
my_room.append(Room("This room has a yellow walls. It feels happy in here."))
my_room.append(Room("This room has a toilet."))
my_room.append(Room("This room has a running machine."))
my_room.append(Room("This room has a many mirrors. Creepy..."))
my_room.append(Room("DEAD END."))


#-------- Room directions 
#Start is North of room 1
my_room[0].setSouth(my_room[1])
my_room[1].setNorth(my_room[0])
#Room 2 is east of room 1
my_room[1].setEast(my_room[2])
my_room[2].setWest(my_room[1])
#Room 3 is esast of room 2
my_room[2].setEast(my_room[3])
my_room[3].setWest(my_room[2])
#Room 4 is esast of room 3
my_room[3].setEast(my_room[4])
my_room[4].setWest(my_room[3])
#Room 5 is esast of room 4
my_room[4].setEast(my_room[5])
my_room[5].setWest(my_room[4])
#Room 6 is esast of room 5
my_room[5].setEast(my_room[6])
my_room[6].setWest(my_room[5])
#room 7
my_room[6].setNorth(my_room[7])
my_room[7].setSouth(my_room[6])
#room 8 -- EXIT
my_room[7].setNorth(my_room[8])
my_room[8].setSouth(my_room[7])

#dead end pathway 
#room 9
my_room[0].setNorth(my_room[9])
my_room[9].setSouth(my_room[0])
#room 10
my_room[9].setEast(my_room[10])
my_room[10].setWest(my_room[9])
#room 11
my_room[10].setNorth(my_room[11])
my_room[11].setSouth(my_room[10])
#room 12
my_room[11].setEast(my_room[12])
my_room[12].setWest(my_room[11])
#room 13
my_room[12].setNorth(my_room[13])
my_room[13].setSouth(my_room[12])
#room 14
my_room[13].setEast(my_room[14])
my_room[14].setWest(my_room[13])

#Make a maze!
#Set the start and exit rooms.
my_maze = Maze(my_room[0],my_room[8])

res = 0
res1 = 0
print(my_maze.getCurrent())
while res1 != 1:    
    T = my_maze.atExit()
    if T == True:
        print('You have found the exit')
        res1 = 1
    else:   
        user_input = input('Enter direction to move north west east south reset: \n')
        if user_input == 'north':
            T = my_maze.moveNorth()
            if T == False:
                print('Direction invalid, try again.')
            else:
                print('You went North.')
                print(my_maze.getCurrent())
                res = 1
        elif user_input == 'south':
            T = my_maze.moveSouth()
            if T == False:
                print('Direction invalid, try again.')              
            else:
                print('You went South.')
                print(my_maze.getCurrent())
                res = 1
        elif user_input == 'west':
            T = my_maze.moveWest()
            if T == False:
                print('Direction invalid, try again.')               
            else:
                print('You went West.')
                print(my_maze.getCurrent())
                res = 1
        elif user_input == 'east':
            T = my_maze.moveEast()
            if T == False:
                print('Direction invalid, try again.')
            else:
                print('You went East.')
                print(my_maze.getCurrent())
                res = 1
        elif user_input == 'reset':
            my_maze.reset()
            print('You went back to the start!')
            print(my_maze.getCurrent())
            res = 1
        else:
            print('Direction invalid, try again.')
            
            
                
            
 
