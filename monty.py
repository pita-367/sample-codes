#Pushpita Rahman
#CS 171-063

"""
This code below simulates a monty python scenario where it displays to the player their chances of winning if they stay with the door they chose or if they win when they switch.
"""
import random
import sys

random.seed(10)

#this function randomizes the door sequence 
def setupDoors():
    doors=['G','G','C']
    random.shuffle(doors)
    return doors

#this function outputs the door the player selected
def playerDoor():
    global user_door_choice
    user_door_choice=random.randint(1,3)
    return user_door_choice

#this function is a door that the player did not select but has the door with the goat is selected (to be shown to player)
def montyDoor(Doors, Player):
    i=0
    door_with_goat=[]
    for item in Doors:
        if item=='G':
            door_with_goat=i+1
            if door_with_goat!=Player:
                door_monty_selected=door_with_goat
                break
        i+=1
    return door_monty_selected

#this function displays a 1 if player stays with the door and it contains a car and they win or 0 if they win when they switch doors
def playRound():
    if player_door_item=='C':
        round_result=0
    else:
        round_result=1
    return round_result

#main program 
if __name__=="__main__":
    print('Welcome to Monty Hall Analysis')
    print('Enter ''exit'' to quit.')

#define variable; used a str to include a str answer 
    num_tests_run='0'

#while the user does not enter exit, keep doing this loop
    while num_tests_run !='exit':
          num_tests_run=''
          num_tests_run=input('How many tests should we run?\n')
#if user says exit, leave the program
          if num_tests_run=='exit':
              print('Thank you for using this program.')
              sys.exit()
#if not, run the game
          else:
              try:
#first, try to convert the input into an integer
                  j=0
                  k=0
                  num_tests_run=int(num_tests_run)
#loop this section from 0 to number of tests the user wants to run.

#first, it runs the door function, then the players function and defines what the user selected. next, it runs the monty door function that shows the door monty picked, and finally, it runs the play round function to say how the player wins (by switching or staying)

                  for test in range(num_tests_run):
                      Doors=setupDoors()
                      Player=playerDoor()
                      player_door_item=Doors[Player-1]
                      door_monty_selected=montyDoor(Doors, Player)
                      round_result=playRound()
#if its 0 then sum up the # of times stay one; else if its 1 sum up times switch one
                      if round_result==0:
                          j+=1
                      else:
                          k+=1
#converts the numbers to percentage and displays to user 
                  stay_percent= j/(j+k)
                  switch_percent= k/(j+k)
                  print('Stay Won', round((stay_percent*100),2), '% of the time.')
                  print('Switch Won', round((switch_percent*100),2),'% of the time.')
                  continue
#if it's not an integer, ask user for a number
              except ValueError as e:
                  print('Please enter a number:')

