import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

print("Welcome to the PyPassword Generator!")
numberLetters= int(input("How many letters would you like in your password?\n")) 
numberSymbols = int(input(f"How many symbols would you like?\n"))
numberNumbers = int(input(f"How many numbers would you like?\n"))

password = []
for i in range(numberLetters):
    password.append(str(letters[r.randint(0,len(letters)-1)]))
for i in range(numberSymbols):
    password.append(str(symbols[r.randint(0,len(symbols)-1)]))
for i in range(numberNumbers):
    password.append(str(numbers[r.randint(0,len(numbers)-1)]))
    
    
r.shuffle(password)
password = ''.join(password)
print(f'Your password is: {password}')
