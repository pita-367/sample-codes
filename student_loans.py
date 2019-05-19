##Pushpita Rahman
#CS 171- 063
#HW 1
#10/13/17

#this is a program that lets the user know loan information
#only for 4 years students

#asks user to input the principle amount of money and for how many years
print ('Welcome to Student Loan Calculator')
print ('Enter the amount of the loan in dollars (no commas):')
principle = int(input())
print ('Enter the number of years the loan will be for:')
years= int(input())

#variables defined
time= 12 					#time paid per yr (same for all loans)
int_sub= 0.034 					#interest for subsidized
int_sub_perc=round((int_sub*100),1)		#interest for subsidized in percentage *1 digit rounding
int_unsub=0.068					#interest for unsubsidized
int_unsub_perc=round((int_unsub*100),1)	#interest for unsubsidized in percentage *1 digit rounding
int_plus= 0.079					#interest for plus
int_plus_perc=round((int_plus*100),1)		#interest for plus in percentage *1 digit rounding
fee_sub= 0.01051 				#fee for subsidized AND unsubsidized
fee_plus= 0.04204				#fee for plus 


#below are calculations for subsidized loan
#all numbers rounded to 2 digits after decimal point unless otherwise stated

#monthly payments 
expnum= -years*time	 			#exponent calculation; same for all three calculations
densub= time*(1-(1+ (int_sub/time))**expnum)	#denominator calculation
numsub= principle*int_sub			#numerator calculation
monthly_pay_sub=numsub/densub			#monthly payments calculation (for subsidized loan)

#total amount
tot_pay_sub= monthly_pay_sub*time*years	#total paid  (for subsidized loan)

#interest paid
int_pay_sub=tot_pay_sub-principle		#interest paid (for subsidized loan)

#fees paid
fee_pay_sub=principle*fee_sub			#amount of fee paid (for subsidized loan)

#total cost
tot_cost_sub=int_pay_sub+fee_pay_sub		#total amount of fees paid (for subsidized loan)

#rounding numbers to 2 digits
monthly_pay_sub_r=round(monthly_pay_sub,2)
tot_pay_sub_r=round(tot_pay_sub,2)
int_pay_sub_r=round(int_pay_sub,2)
fee_pay_sub_r=round(fee_pay_sub,2)
tot_cost_sub_r=round(tot_cost_sub,2)

#display ans for subsidized
print ("\n")
print ('Subsidized Federal Direct Loan')
print ("Principle: $", principle)
print ("Interest Rate:", int_sub_perc, "%")
print ("Years:",years)
print ("Monthly Payment: $",monthly_pay_sub_r)
print ("Total Paid on Loan: $",tot_pay_sub_r)
print ("Total Interest Paid: $",int_pay_sub_r,)
print ("Additional Fees Paid: $",fee_pay_sub_r)
print ("Total Cost Over Principle: $",tot_cost_sub_r)
print ("\n")


#below are calculations for unsubsidized loan
#all numbers rounded to 2 digits after decimal point unless otherwise stated

principle_unsub=principle*(1+(int_unsub*4.25))		#new principle (unsub) amount b/c interest starts as soon as loan is taken

#monthly payments 
denunsub= time*(1-(1+ (int_unsub/time))**expnum)	#denominator calculation
numunsub= principle_unsub*int_unsub				#numerator calculation
monthly_pay_unsub=numunsub/denunsub			#monthly payments calculation (for unsubsidized loan)

#total amount
tot_pay_unsub= monthly_pay_unsub*time*years	#total paid  (for unsubsidized loan)

#interest paid
int_pay_unsub=tot_pay_unsub-principle		#interest paid (for unsubsidized loan)

#fees paid
fee_pay_unsub=principle*fee_sub			#amount of fee paid (for unsubsidized loan)

#total cost
tot_cost_unsub=int_pay_unsub+fee_pay_unsub		#total amount of fees paid (for unsubsidized loan)

#rounding numbers to 2 digits
monthly_pay_unsub_r=round(monthly_pay_unsub,2)
tot_pay_unsub_r=round(tot_pay_unsub,2)
int_pay_unsub_r=round(int_pay_unsub,2)
fee_pay_unsub_r=round(fee_pay_unsub,2)
tot_cost_unsub_r=round(tot_cost_unsub,2)

#display ans for unsubsidized

print ('Unsubsidized Federal Direct Loan')
print ("Principle: $", principle)
print ("Interest Rate:", int_unsub_perc, "%")
print ("Years:",years)
print ("Monthly Payment: $",monthly_pay_unsub_r)
print ("Total Paid on Loan: $",tot_pay_unsub_r)
print ("Total Interest Paid: $",int_pay_unsub_r,)
print ("Additional Fees Paid: $",fee_pay_unsub_r)
print ("Total Cost Over Principle: $",tot_cost_unsub_r)
print ("\n")


#below are calculations for plus loan
#all numbers rounded to 2 digits after decimal point unless otherwise stated
	
principle_plus=principle*(1+(int_plus*4.25))		#new principle (plus) amount b/c interest starts as soon as loan is taken

#monthly payments 
denplus= time*(1-(1+ (int_plus/time))**expnum)		#denominator calculation
numplus= principle_plus*int_plus				#numerator calculation
monthly_pay_plus=numplus/denplus				#monthly payments calculation (for plus loan)

#total amount
tot_pay_plus= monthly_pay_plus*time*years	#total paid  (for unsubsidized loan)

#interest paid
int_pay_plus=tot_pay_plus-principle		#interest paid (for unsubsidized loan)

#fees paid
fee_pay_plus=principle*fee_plus			#amount of fee paid (for unsubsidized loan)

#total cost
tot_cost_plus=int_pay_plus+fee_pay_plus		#total amount of fees paid (for unsubsidized loan)

#rounding numbers to 2 digits
monthly_pay_plus_r=round(monthly_pay_plus,2)
tot_pay_plus_r=round(tot_pay_plus,2)
int_pay_plus_r=round(int_pay_plus,2)
fee_pay_plus_r=round(fee_pay_plus,2)
tot_cost_plus_r=round(tot_cost_plus,2)

#display ans for plus

print ('Federal PLUS Loan')
print ("Principle: $", principle)
print ("Interest Rate:", int_plus_perc, "%")
print ("Years:",years)
print ("Monthly Payment: $",monthly_pay_plus_r)
print ("Total Paid on Loan: $",tot_pay_plus_r)
print ("Total Interest Paid: $",int_pay_plus_r,)
print ("Additional Fees Paid: $",fee_pay_plus_r)
print ("Total Cost Over Principle: $",tot_cost_plus_r)
print ("\n")



