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
				print("\nError: Improper value inputted.")

	while True: # While loop allows program to continue running when exceptions occur.
		try:
			p = float(input("\nEnter the Principal amount: $"))
			if p == 0:
				raise Exception
			elif p < 0:
				raise Exception
			break
		except:
			print("\nError: Improper value inputted.")

	while True: # While loop allows program to continue running when exceptions occur.
		try:
			r = float(input("\nEnter an Interest rate: %"))
			if r < 0:
				raise Exception
			break
		except:
			print("\nError: Interest rate cannot be negative.")

	answer = math.log10(a/p) / (math.log10(1 + (r/100)))
	print("\nThe number of years compounded is roughly %s." % round(answer, 2))


if __name__ == '__main__':
	print("FileError: Unable to run directy, use run.py instead.\n")
	input("Press ENTER to exit.")
