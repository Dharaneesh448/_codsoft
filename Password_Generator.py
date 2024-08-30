import random
import string
x=int(input("Enter the desired length of your password:"))
characters = string.ascii_letters + string.digits + '_' +'.'
password = ''.join(random.choice(characters) for _ in range(x))
print("Generated Password:", password)
