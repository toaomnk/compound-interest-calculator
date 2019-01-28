import math
print("[1] Accumulated Amount [2] Principal [3] Interest Rate [4] Years \n")
var = input("What do you want to solve for? ")

if var == str(1):
	p = float(input("\nPlease enter the Principal amount: $"))
	r = float(input("Please enter an Interest rate: %"))
	n = int(input("Please enter the number of times compounded in a year: "))
	t = int(input("Please enter the number of years compounded: "))
elif var == str(2):
	a = float(input("\nPlease enter the Accumulated amount: $"))
	r = float(input("Please enter an Interest rate: %"))
	n = int(input("Please enter the number of times compounded in a year: "))
	t = int(input("Please enter the number of years compounded: "))
elif var == str(3):
	a = float(input("\nPlease enter the Accumulated amount: $"))
	p = float(input("Please enter the Principal amount: $"))
	n = int(input("Please enter the number of times compounded in a year: "))
	t = int(input("Please enter the number of years compounded: "))
elif var == str(4):
	a = float(input("\nPlease enter the Accumulated amount: $"))
	p = float(input("Please enter the Principal amount: $"))
	r = float(input("Please enter an Interest rate: %"))	
	n = int(input("Please enter the number of times compounded in a year: "))

try: 
	accumulated_amount = float(p * (1 + ((r/100)/n)) ** (n * t))
except: 
	if var == str(1):
		print("\nThere has been an error calculating the accumulated amount.\n")
try: 
	principal_amount = float(a / (1 + ((r/100)/n)) ** (n * t))
except: 
	if var == str(2):
		print("\nThere has been an error calculating the principal amount.\n")
try: 
	interest_rate = float((((a/p) ** (1/nt)) - 1) * n)
except:
	if var == str(3):
		print("\nThere has been an error calculating the interest rate.\n")
try: 
	number_of_years = ((math.log10(a/p) / n(math.log10(1 + (r/100)/n))))
except:
	if var == str(4):
		print("\nThere has been an error calculating the number of years compounded.\n")

if var == str(1):
	try: print("\nThe accumulated amount is $%s.\n" % round(accumulated_amount, 2))
	except:
		pass
if var == str(2):
	try: print("\nThe principal amount is $%s.\n" % round(principal_amount, 2))
	except:
		pass
if var == str(3): 
	try: print("\nThe interest rate is $%s.\n" % interest_rate)
	except:
		pass
if var == str(4):
	try: print("\nThe number of years compounded is $%s.\n" % round(number_of_years, 2))
	except:
		pass

input("Press Enter to exit. ")