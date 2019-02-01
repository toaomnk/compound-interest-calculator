import math

print("[1] Accumulated Amount [2] Principal [3] Interest Rate [4] Years \n")
var = int(input("What do you want to solve for? "))

def r_of_c():	# What gets assigned here is based upon the user's input based on its corrosoponding function.
	roc = int(input("\nEnter the rate of compounding: "))
	if roc == 1:
		n = 365
	elif roc == 2:
		n = 52
	elif roc == 3:
		n = 12
	elif roc == 4:
		n = 4
	elif roc == 5:
		n = 2
	elif roc == 6:
		n = 1
	elif roc == 7:
		n = 2.7182
	elif roc > 7:
		error.input()
	elif roc < 1:
		error.input()
	else:
		error.input()
class error: # All possible errors are located here.
	def input():
		print("\nError: Invalid input entered.\n")
	def accumulated():
		print("\nError: There has been an error calculating the accumulated amount.\n")
	def principal():
		print("\nError: There has been an error calculating the principal amount.\n")
	def rate():
		print("\nError: There has been an error calculating the interest rate.\n")
	def years():
		print("\nError: There has been an error calculating the number of years.\n")
class user_input:
	def one():
		if var == 1:
			p = float(input("\nPlease enter the Principal amount: $"))
			r = float(input("\nPlease enter an Interest rate: %"))
			print("\n[1] Daily [2] Weekly [3] Monthly [4] Quarterly [5] Semi-Annually [6] Annually [7] Continuously")
			r_of_c()
			t = int(input("\nPlease enter the number of years compounded: "))
			accumulated_amount = float(p * (1 + ((r/100)/n)) ** (n * t))
		else:
			pass
	def two():
		if var == 2:
			a = float(input("\nPlease enter the Accumulated amount: $"))
			r = float(input("\nPlease enter an Interest rate: %"))
			print("\n[1] Daily [2] Weekly [3] Monthly [4] Quarterly [5] Semi-Annually [6] Annually [7] Continuously")
			r_of_c()
			print(roc)
			t = int(input("\nPlease enter the number of years compounded: "))
			try: principal_amount = float(a / (1 + ((r/100)/n)) ** (n * t))
			except: 
				error.principal()
		else:
			pass
	def three():
		if var == 3:
			a = float(input("\nPlease enter the Accumulated amount: $\n"))
			p = float(input("\nPlease enter the Principal amount: $"))
			print("\n[1] Daily [2] Weekly [3] Monthly [4] Quarterly [5] Semi-Annually [6] Annually [7] Continuously")
			r_of_c()
			t = int(input("\nPlease enter the number of years compounded: "))
			try: interest_rate = float(n(math.pow(a/p, 1/nt) - 1))
			except:
				error.rate()
		else:
			pass
	def four():
		if var == 4:
			a = float(input("\nPlease enter the Accumulated amount: $\n"))
			p = float(input("\nPlease enter the Principal amount: $"))
			r = float(input("\nPlease enter an Interest rate: %"))	
			print("\n[1] Daily [2] Weekly [3] Monthly [4] Quarterly [5] Semi-Annually [6] Annually [7] Continuously")
			r_of_c()
			t = int(input("\nPlease enter the number of years compounded: "))
			try: number_of_years = ((math.log10(a/p) / n(math.log10(1 + (r/100)/n))))
			except:
				error.years()
		else:
			pass
	def greater_than():
		if var > 4:
			error.input()
		else:
			pass
	def less_than():
		if var < 1:
			error.input()
		else: 
			pass
class answer: # This will be processed based upon the intial user input.
	def one():
		if var == (1):
			try: print("\nThe accumulated amount is $%s.\n" % round(accumulated_amount, 2))
			except:
				pass
	def two():
		if var == (2):
			try: print("\nThe principal amount is $%s.\n" % round(principal_amount, 2))
			except:
				pass
	def three():
		if var == (3): 
			try: print("\nThe interest rate is $%s.\n" % interest_rate)
			except:
				pass
	def four():
		if var == (4):
			try: print("\nThe number of years compounded is $%s.\n" % round(number_of_years, 2))
			except:
				pass 	

""" The following will process the users input based on which function it gets assigned to. """

user_input.one() 
user_input.two()
user_input.three()
user_input.four()
user_input.greater_than() 
user_input.less_than()

""" The following will output the answer based on the initial user input. """

answer.one()
answer.two()
answer.three() 
answer.four()		

input("Press Enter to exit. ")
