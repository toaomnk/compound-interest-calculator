def calculate():
	a = float(input("\nEnter the Accumulated amount: $"))
	r = float(input("\nEnter an Interest rate: %"))
	print("\n[1] Daily [2] Weekly [3] Monthly [4] Quarterly [5] Semi-Annually [6] Annually [7] Continuously")
	c = int(input("\nEnter the rate of compounding: "))
	if c == 1:
		n = 365
	elif c == 2:
		n = 52
	elif c == 3:
		n = 12	
	elif c == 4:
		n = 4
	elif c == 5:
		n = 2
	elif c == 6:
		n = 1
	elif c == 7:
		n = 2.7182
	t = int(input("\nEnter the number of years compounded: "))
	answer = float(a / (1 + ((r/100)/n)) ** (n * t))
	print("\nThe principal amount is $%s." % round(answer, 2))

if __name__ == '__main__':
	print("FileError: Unable to run directy, use calculator.py instead.\n")
	input("Press ENTER to exit.")
