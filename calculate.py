from formulas import accumulated_amount
from formulas import principal
from formulas import rate
from formulas import years

print("[1] Accumulated Amount [2] Principal [3] Interest Rate [4] Years")
while True:
	try:
		var = int(input("\nWhat are you solving for?: "))
		if var > 4:
			raise Exception("\nError: Improper value inputed.")
		if var < 1:
			raise Exception("\nError: Improper value inputed.")
		break
	except:
		print("\nError: Improper value inputed.")
		
if var == 1:
	accumulated_amount.calculate()
elif var == 2:
	principal.calculate()
elif var == 3:
	rate.calculate()
elif var == 4:
	years.calculate()

input("\nPress ENTER to exit.")
