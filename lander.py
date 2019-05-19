#Pushpita Rahman
#Computer Programming I
#12/8/17

"""
This program is a game players can play to simulate a planet landing.
Goal: pilot the lunar lander to a safe landing.

the program first asks the user to select how much fuel to use and based on answer, altitude and velocity would change.
this would continue until altitude reaches 0 where the lunar has landed (this is exlained further in play_level function

this game has many levels starting from the moon all the way to the sun (total of 11 levels)
you can only move up to the next level once you pass the previous level or quit the game
"""


import sys

#defines what planet is for each level (decided to keep the same order for the levels)
level_with_planet={1:'Moon',
                   2:'Earth',
                   3:'Pluto',
                   4:'Neptune',
                   5:'Uranus',
                   6:'Saturn',
                   7:'Jupiter',
                   8:'Mars',
                   9:'Venus',
                   10:'Mercury',
                   11:'Sun'}
                
#defines the gravity for each planet                             
planet_gravity={'Moon':-1.622,
                'Earth':-9.81,
                'Pluto':-0.42,
                'Neptune':-14.07,
                'Uranus':-10.67,
                'Saturn':-11.08,
                'Jupiter':-25.95,
                'Mars':-3.77,
                'Venus':-8.87,
                'Mercury':-3.59,
                'Sun':-274.13}



"""
Function ask_fuel asks user to enter how much fuel should be burned. however, there are
certain critera to be met:
1) must be a positive
2) a non-decimal amount
3) must be less than or equal to current amount of fuel
the function will keep asking the user for a value until all three criteria is met.
"""

def ask_fuel(current_fuel):
    global fuel_to_burn
    fuel_to_burn=input('Enter units of fuel to use: ')
    #try to convert to integer
    try:
        fuel_to_burn=int(fuel_to_burn)
        #if it is a positive number and less than the current fuel amount then keep number as is (what will be returned)
        if fuel_to_burn >= 0 and fuel_to_burn <= current_fuel:
            fuel_to_burn=fuel_to_burn
        #if its less than 0, then tell user cant have negative number and repeat through function again until postive number
        elif fuel_to_burn < 0 :
            print('Cannot use negative value.')
            ask_fuel(current_fuel)
        #if its greater than current fuel amount then tell user not enough fuel and print current amount of fuel available and repeat through function again until criteria is met
        elif fuel_to_burn > current_fuel:
            print('Not enough fuel. Max Fuel:',current_fuel)
            ask_fuel(current_fuel)
    #if it's not an integer, tell user to enter a number and go through function again until its an integer value              
    except ValueError as e:
        print('Please Enter Integer Value.')
        ask_fuel(current_fuel)
    
    return fuel_to_burn  

"""
Function play_level plays the game
first all variables are defined and shown to the user
then it asks user how much fuel to burn using ask_fuel function
this repeats until altitude reaches 0
one altitude reaches 0, the game concludes
if velocity is within +/- 2m then the player successfully landed, if not they crashed

the result of the game is place in a variable because this will allow later on to see if the player passed the level (if they didn't pass level, they would play level again)

"""

def play_level(name, G, fuel):
    global result
    #defines initial values 
    altitude=50         #Altitude (m)
    velocity=0          #intial velocity (m/s)
    second=0            #seconds
    thruster_acceleration=0.1 # (m/s2)

    #print intial values to user
    print('Landing on the',name)
    print('Gravity is', G,'m/s^2')
    print('Initial Altitude: ',altitude, 'meters')
    print('Intital Velocity: ', velocity,'m/s')
    print('Burning a unit of fuel causes 0.10 m/s slowdown.')
    print('Initial Fuel Level: ', fuel,'units')
    print()
    print('GO \n')

    #while altitude is greater than 0 play the game; ask user how to fuel to burn and use ask_fuel function
    while altitude > 0:       
        fuel_to_burn=ask_fuel(fuel)
        fuel= fuel - fuel_to_burn
        velocity= velocity + G + thruster_acceleration * fuel_to_burn
        altitude=altitude+velocity
        second+=1

        #if altitude is less than 0 make altitude 0 (because we can't have negative altitude)
        if altitude < 0:
            altitude=0

        #print to user current stats     
        print('After',second,'seconds Altitude is', round(altitude,2),'meters, velocity is',round(velocity,2),'m/s.')
        print('Remaining Fuel: ', fuel,'units')
    
    #if between +/-2, then successful landing, else crash landing       
    if -2 <= velocity <= 2:
        result='Landed Successfully.'
    else:
        result='Crashed!'
        
    print(result)
    return result
        
    
"""
main function
play each level until user passes the level or does not want to play any more

first, ask if they want to play level
if yes, then enter game and use function play_level to play the level
if the player crashes, then the player has to replay the level they failed; else they can play the next level (or if they say no, they exit the system)

"""
if __name__=="__main__":
    print('Welcome to Lunar Lander Game')
    level=1
    continue_game=''
    #while player does not enter no, play the game
    while continue_game!='no':
        print('Do you want to play Level',level,'? (yes/no)')
        continue_game=input()     
        if continue_game=='yes':
            print('Entering Level',level)
            name=level_with_planet[level] #gets the planet of the level
            G=planet_gravity[name]       #gets gravity for the planey
            if level==1:                #level 1 (moon) must start with 150 units of fuel
                fuel=150
            else:                       #any other level, the fuel is 150 times the level they are on
                fuel=150*level
            play_level(name, G, fuel)   #play the level
            #if they crashed, they replay that level; if they pass, they move up to next level
            if result=='Crashed!':      
                level=level
            else:
                level+=1

        #when they don't want to continue game any more, print to user how many levels they completed and exit the system.        
        elif continue_game=='no':
            print('You made it past',level-1,'levels.')
            print('Thank you for playing!')
            sys.exit()

            


