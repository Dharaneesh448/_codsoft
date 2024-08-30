'''
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=input("Enter the operation(add/sub/mult/div/square):")
d=0

if c == "add":
    d=a+b
    print("The answer is:",d)
elif c =="sub":
    d=a-b
    print("The answer is:",d)
elif c == "mult":
    d=a*b
    print("The answer is:",d)
elif c== "div":
    d=a/b
    print("The answer is:",d)
elif c == "square":
    d=a**b
    print("The answer is:",d)
else:
    print("Invalid input/operation")
'''
import string

# Prompt the user to specify the desired length of the password
length = int(input("Enter the desired length of the password: "))
x=string.ascii_letters

for i in range(length):
    password=random.choice(x)
    print(password)