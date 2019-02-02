import math

def calculate():
	while True:
			try:
				a = float(input("\nEnter the Accumulated amount: $"))
				break
			except:
				print("\nError: Improper value inputed.")
	while True:
		try:
			p = float(input("\nEnter the Principal amount: $"))
			if p == 0:
				raise Exception("\nError: Cannot divide by zero.")
			break
		except:
			print("\nError: Improper value inputed.")
	while True:
		try:
			r = float(input("\nEnter an Interest rate: %"))
			if r == 0:
				raise Exception("\nError: Improper value inputed.")
			break
		except:
			print("\nError: Improper value inputed.")

	answer = math.log10(a/p) / (math.log10(1 + (r/100)))
	print("\nThe number of years compounded is %s." % round(answer, 2))

if __name__ == '__main__':
	print("FileError: Unable to run directy, use calculator.py instead.\n")
	input("Press ENTER to exit.")
