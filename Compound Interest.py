import math

print("[1] Accumulated Amount [2] Principal [3] Interest Rate [4] Years \n")

var = int(input("What do you want to solve for? "))

if var == (1):
	p = float(input("\nPlease enter the Principal amount: $"))

	r = float(input("\nPlease enter an Interest rate: %"))

	print("\n[1] Daily [2] Weekly [3] Monthly [4] Quarterly [5] Semi-Annually [6] Annually [7] Continuously")

	r_of_c = input("\nEnter the rate of compounding: ")
	if r_of_c == str(1):
		n = 365
	elif r_of_c == str(2):
		n = 52
	elif r_of_c == str(3):
		n = 12
	elif r_of_c == str(4):
		n = 4
	elif r_of_c == str(5):
		n = 2
	elif r_of_c == str(6):
		n = 1
	elif r_of_c == str(7):
		n = 2.7182
	elif r_of_c > 7:
		print("Invalid input entered.")
	elif r_of_c < 1:
		print("Invalid input entered.")
	else:
		pass

	t = int(input("\nPlease enter the number of years compounded: "))

elif var == (2):
	a = float(input("\nPlease enter the Accumulated amount: $"))

	r = float(input("\nPlease enter an Interest rate: %"))

	print("\n[1] Daily [2] Weekly [3] Monthly [4] Quarterly [5] Semi-Annually [6] Annually [7] Continuously")

	r_of_c = input("\nEnter the rate of compounding: ")
	if r_of_c == (1):
		n = 365
	elif r_of_c == (2):
		n = 52
	elif r_of_c == (3):
		n = 12
	elif r_of_c == (4):
		n = 4
	elif r_of_c == (5):
		n = 2
	elif r_of_c == (6):
		n = 1
	elif r_of_c == (7):
		n = 2.7182
	elif r_of_c > 7:
		print("Invalid input entered.")
	elif r_of_c < 1:
		print("Invalid input entered.")
	else:
		pass

	t = int(input("\nPlease enter the number of years compounded: "))

elif var == (3):
	a = float(input("\nPlease enter the Accumulated amount: $\n"))

	p = float(input("\nPlease enter the Principal amount: $"))

	print("\n[1] Daily [2] Weekly [3] Monthly [4] Quarterly [5] Semi-Annually [6] Annually [7] Continuously")

	r_of_c = input("\nEnter the rate of compounding: ")
	if r_of_c == (1):
		n = 365
	elif r_of_c == (2):
		n = 52
	elif r_of_c == (3):
		n = 12
	elif r_of_c == (4):
		n = 4
	elif r_of_c == (5):
		n = 2
	elif r_of_c == (6):
		n = 1
	elif r_of_c == (7):
		n = 2.7182
	elif r_of_c > 7:
		print("Invalid input entered.")
	elif r_of_c < 1:
		print("Invalid input entered.")
	else:
		pass

	t = int(input("\nPlease enter the number of years compounded: "))

elif var == (4):
	a = float(input("\nPlease enter the Accumulated amount: $\n"))
	p = float(input("\nPlease enter the Principal amount: $"))
	r = float(input("\nPlease enter an Interest rate: %"))	
	print("\n[1] Daily [2] Weekly [3] Monthly [4] Quarterly [5] Semi-Annually [6] Annually [7] Continuously")
	r_of_c = input("\nEnter the rate of compounding: ")
	if r_of_c == (1):
		n = 365
	elif r_of_c == (2):
		n = 52
	elif r_of_c == (3):
		n = 12
	elif r_of_c == (4):
		n = 4
	elif r_of_c == (5):
		n = 2
	elif r_of_c == (6):
		n = 1
	elif r_of_c == (7):
		n = 2.7182
	elif r_of_c > 7:
		print("Invalid input entered.")
	elif r_of_c < 1:
		print("Invalid input entered.")
	else:
		pass

elif var > 4:
	print("\nError: Incorrect input entered.\n")

elif var < 1:
	print("\nError: Incorrect input entered.\n")

if var == (1): 
	try: 
		accumulated_amount = float(p * (1 + ((r/100)/n)) ** (n * t))
	except:
		print("\nThere has been an error calculating the accumulated amount.\n")
		input("Press Enter to exit. ")

elif var == (2): 
	try:
		principal_amount = float(a / (1 + ((r/100)/n)) ** (n * t))
	except: 
		print("\nThere has been an error calculating the principal amount.\n")
		input("Press Enter to exit. ")

elif var == (3): 
	try:
		interest_rate = float(n(math.pow(a/p, 1/nt) - 1))
	except:
		print("\nThere has been an error calculating the interest rate.\n")
		input("Press Enter to exit. ")

elif var == (4): 
	try:
		number_of_years = ((math.log10(a/p) / n(math.log10(1 + (r/100)/n))))
	except:
		print("\nThere has been an error calculating the number of years compounded.\n")
		input("Press Enter to exit. ")

if var == (1):
	try:
		print("\nThe accumulated amount is $%s.\n" % round(accumulated_amount, 2))
	except:
		pass

elif var == (2):
	try: print("\nThe principal amount is $%s.\n" % round(principal_amount, 2))
	except:
		pass

elif var == (3): 
	try: print("\nThe interest rate is $%s.\n" % interest_rate)
	except:
		pass

elif var == (4):
	try: print("\nThe number of years compounded is $%s.\n" % round(number_of_years, 2))
	except:
		pass

input("Press Enter to exit. ")
