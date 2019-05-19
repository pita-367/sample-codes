#!/usr/bin/env python3
#
# calc.py -- calculator that parses an infix expression into postfix, then evaluates it in command line
# Assumptions: all inputs are valid inputs (does error checking for Division by 0)
#
# Pushpita Rahman
# Advanced Programming Techniques
#
#
# Python 3.6
# on Linux 4.4.0-134-generic #160-Ubuntu
# 
# EDITOR: tabstop=2, cols=125


import sys
#function infix2postfix -- takes an infix expression and converts to a postfix expression
def infix2postfix(expression):
	#separate tokens by whitespace
	expression = expression.split(" ")
	main_stack = [] #main output stack
	aux_stack = []  #auxillary stack to store operands
        	
   #dictionary to set precedence 
	prec = {
   	"+": 1,
        "-": 1,
     	"*": 2,
     	"/": 2,
     	"%": 2,
     	"(": 0, 
     	")": 3}
    
  	#loop through each token 
	for i in range(len(expression)):
   	#first check to see if token is a number, if so add to main stack
		try:
			type(int(expression[i])) == type(1)
			main_stack.append(int(expression[i]))

     	#if not (will produce a ValueError), it's an operator    
		except ValueError as e:
			j = len(aux_stack)
	
			#if aux stack has more than 1 operator, then compare the previous operator
			#if it's greater or equal to current operator, pop it put in in the main stack
			if j >= 1 and expression[i] != '(':
				if prec[aux_stack[j-1]] >= prec[expression[i]]:
					op = aux_stack.pop()
					main_stack.append(op)
					aux_stack.append(expression[i])
         	#handles the (eqn ): if a right ) is found, then pop the operator and add to main stack until the left ( is found 
				elif expression[i] == ')':
					if aux_stack != '(':
						op = aux_stack.pop()
						main_stack.append(op)
						aux_stack.pop()                       
            	#if less precendent then just append operator to aux stack
				else:
						aux_stack.append(expression[i])
            
      	#if none of rules apply above, just append operator to aux stack
			else:
				aux_stack.append(expression[i])
                           
    #expression is finished looping, pop off and append each of the operators remaining in aux stack       
	for j in range(len(aux_stack)):
		op = aux_stack.pop()
		main_stack.append(op)              
                
	return main_stack

#function evalPostfix -- evaluates a postfix expression
def evalPostfix(stack):
	eval_stack = [] #evaluated stack
	"""
        For each token in the stack, see if token is operator:
        if so pop it (sign), 2nd pop = integer 2 and 3rd pop = integer 1
        evalaute two integers and append the value to the evalstack
        """
	for i in range(len(stack)):     
		eval_stack.append(stack[i])	
		if stack[i] == '+':           
			sign = eval_stack.pop()
			int2 = eval_stack.pop()
			int1 = eval_stack.pop()
			value = int(int1) + int(int2)
			eval_stack.append(value)
		elif stack[i] == '*':
			sign = eval_stack.pop()
			int2 = eval_stack.pop()
			int1 = eval_stack.pop()
			value = int(int1) * int(int2)
			eval_stack.append(value)
		elif stack[i] == '-':
			sign = eval_stack.pop()
			int2 = eval_stack.pop()
			int1 = eval_stack.pop()
			value = int(int1) - int(int2)
			eval_stack.append(value)
		elif stack[i] == '/':
			sign = eval_stack.pop()
			int2 = eval_stack.pop()
			int1 = eval_stack.pop()
			try: 
				value = int(int1) / int(int2)
				eval_stack.append(value)
			except ZeroDivisionError: #error checking for division by 0 
				return('Nan') 
		elif stack[i] == '%':
			sign = eval_stack.pop()
			int2 = eval_stack.pop()
			int1 = eval_stack.pop()
			value = int(int1) % int(int2)
			eval_stack.append(value)
            
	return value 


if __name__ == '__main__':
	try: #try statement for error checking
        #checks to see if command line argument is given
		if len(sys.argv) > 1:
			file = open(sys.argv[1],'r')
		else:
			file = sys.stdin
		fileinfo = file.readlines()
		for line in fileinfo: #for each line, run through infix2postfix then evaluate with evalPostfix and print outcome
			line = line.strip('\n')
			postfix = infix2postfix(line)
			postfix_str = " ".join(str(i) for i in postfix)
			output = evalPostfix(postfix)
			print(postfix_str, '=', output)

	except Exception as e:  #print error and exit system
		print(e)
		sys.exit(1)




