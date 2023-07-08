'''
To create a password with Python, we need to create a program 
that takes the length of the password and generates a random password of the same length. 
In this article, I’ll walk you through how to write a Python program to generate a password.
'''
import random

passlen = int(input("enter a password length: "))
asciitable= "bcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
asciiarray = []
for i in range(0,len(asciitable)):
    asciiarray.append(asciitable[i])

createdpass = ""
for i in range(0,passlen):
    createdpass = createdpass + random.choice(asciiarray)

print(createdpass)

'''
ALTERNATIF CODE


import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)

'''