#Pushpita Rahman
#Computer Programming I
#Oct 27, 2017

#code converted lengths 

#creates dictionary using inches as a base
dict_units = {
	'inches': 1,
	'feet': 12,
	'yards': 36,
	'miles': 63360,
	'leagues': 190080,
        'centimeters': 1/2.54,
        'decimeters':10/2.54,
        'meters':10**2/2.54,
        'decameters':10**3/2.54,
        'hectometers': 10**4/2.54,
        'kilometers':10**5/2.54
}

#lets user know what program can do and what units it can take
print('Welcome to the length conversion wizard.')
print('This program can convert between any of the following length.')
print('inches\nfeet\nyards\nmiles\nleagues\ncentimeters\ndecimeters\nmeters\ndecameters\nhectometers\nkilometers')
print('Note: you must use the units exactly as spelled above.\n')

#asks user for inputs
user_val=float(input('Enter value: '))        #asks user for a digit; supports decimals
user_unit=input('Enter from units: ')         #asks user for initial units
converted_units=input('Enter to units: ')     #asks user for units they wish to convert to

val_in_inches=user_val*dict_units[user_unit]      #converts the value into inches
converted_unit_in_inches= dict_units[converted_units] #goes into dictonary to obtain the units in inches for the unit they wish to convert to
converted_val= val_in_inches/converted_unit_in_inches  #converts value to converted unit
converted_val_round4sigfigs=round(converted_val,4)      #rounds value to 4 significant digits

print() #blank line
#prints the answer
print(user_val, user_unit, 'is', converted_val_round4sigfigs, converted_units,'\n')
