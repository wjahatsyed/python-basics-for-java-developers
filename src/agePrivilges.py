#An examle of conditional statements in Python
print("Please enter your age")
age = int(input())
print("Are you a US citizen?")
citizen = bool(input())
if(age >12) and (age<20):
	print("You are a teen ager")
else:
	print("You are a Child!")

if(age<21) or (citizen == False):
	print("Not eligible")
else:
	print("You can vote")