#Example of input
name = input("Please tell me your name")
"""
In Python 3 and above, we can replace raw_input with input
"""
print("Hello" +name+ "Please also tell me your age")
age = int(input())
print("So" +name+ " you are" +str(age)+ "years old, now tell me your height")
height = float(input())
print(name +" "+  str(age) +" "+  str(height))