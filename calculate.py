from formulas import accumulated_amount
from formulas import principal
from formulas import rate
from formulas import years

print("\n[1] Accumulated Amount [2] Principal [3] Interest Rate [4] Years") # Lists sub-calculators available.

while True: # While loop allows program to continue running when exceptions occur.
	try:
		var = int(input("\nWhat are you solving for?: "))
		if var > 4: # var cannot be out of range from 1-4.
			raise Exception
		elif var < 1:
			raise Exception
		break
	except:
		print("\nError: Improper value inputed.")

if var == 1:
	from formulas import accumulated_amount
	accumulated_amount.calculate() # Initilization.

elif var == 2:
	from formulas import principal
	principal.calculate() # Initilization.

elif var == 3:
	from formulas import rate
	rate.calculate() # Initilization.
	
elif var == 4:
	from formulas import years
	years.calculate() # Initilization.
	
input("\nPress ENTER to exit.")
