import random


characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
password = ""
lenght = int(input("Enter the lenght of the password: "))
for i in range(lenght):
    password += random.choice(characters)

print(password)
