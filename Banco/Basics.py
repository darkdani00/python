import random
import math


#HP = 100

#potion = random.randint(25,50) 

#difficult = "Easy mode"

#print(difficult)
#print(HP + potion)

email = input("What is you email?: ")
user = email[:email.index("@")]

domain = email[email.index("@") + 1:]

print(domain)

print(user)


numero = 1
letra = "hola"

print(letra + str(numero))

name  = input("What is your name?: ").strip()
print("Hello " + name)


age  = input("What is your age?: ")
print("Your age is: " + age)

city = input("Which city do you live?: ")
print(city)

enjoy = input("What do you enjoy most?: ")
print(enjoy)