from formulas import accumulated_amount
from formulas import principal
from formulas import rate
from formulas import years

print("\n[1] Accumulated Amount [2] Principal [3] Interest Rate [4] Years")
var = int(input("\nWhat do you want to solve for?: "))

if var == 1:
	accumulated_amount.calculate()
elif var == 2:
	principal.calculate()
elif var == 3:
	rate.calculate()
elif var == 4:
	years.calculate()
	
input("\nPress ENTER to exit.")
