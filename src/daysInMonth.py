month = int(input("Enter the number of month"))
OddOrEven = month%2
if(month== 2):
	print("There are 28 or 29 days in this month")
elif(OddOrEven == 0):
	print("There are 30 days in this month")
else:
	print("There are 31 days in this month")