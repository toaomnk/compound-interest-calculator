import math

def calculate():

	while True: # While loop allows program to continue running when exceptions occur.
		try:
			a = float(input("\nEnter the Accumulated amount: $"))
			if a == 0:
				raise Exception
			elif a < 0:
				raise Exception
			break
		except:
			print("\nError: Improper Value Entered.")

	while True: # While loop allows program to continue running when exceptions occur.
		try:
			p = float(input("\nEnter the Principal amount: $"))
			if p == 0:
				raise Exception
			elif p < 0:
				raise Exception
			break
		except:
			print("\nError: Principal amount cannot be a negative number.")

	while True: # While loop allows program to continue running when exceptions occur.
		try:
			t = float(input("\nEnter the number of years compounded: "))
			if t < 0:
				raise Exception
			break
		except:
			print("\nError: Cannot compound a negative number of years.")

	print("\n[1] Daily [2] Weekly [3] Monthly [4] Quarterly [5] Semi-Annually [6] Annually [7] Continuously")

	while True: # While loop allows program to continue running when exceptions occur.
		try:
			c = int(input("\nEnter the rate of compounding: "))
			if c > 7:
				raise Exception("\nError: Improper Value Entered.")
			elif c < 1:
				raise Exception("\nError: Improper Value Entered.")
			break
		except:
			print("\nError: Improper Value Entered.")

	if c == 1:
		n = 365 # Yearly
	elif c == 2:
		n = 52 # Weekly
	elif c == 3:
		n = 12 # Monthly
	elif c == 4:
		n = 4 # Quarterly
	elif c == 5:
		n = 2 # Biannually
	elif c == 6:
		n = 1 # Yearly
	elif c == 7:
		n = math.e # Continously

	answer = (n * (math.pow(a/p, 1/(n * t)) - 1)) * 100
	print("\nThe interest rate is %s percent." % round(answer, 2))

if __name__ == '__main__':
	print("FileError: Unable to run directy, use run.py instead.\n")
	input("Press ENTER to exit.")
