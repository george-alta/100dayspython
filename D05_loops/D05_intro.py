import random
print("welcome to PyPassword Generator!")
n_letters = int(input("How many letters do you want in your password? "))
n_symbols = int(input("How many symbols do you want in your password? "))
n_numbers = int(input("How many numbers do you want in your password? "))

letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers="1234567890"
symbols="!@#$%^&*()?><"

password = ""
i = 0
while i < n_letters:
    password = password + letters[random.randint(0,len(letters)-1)]
    i +=1

i = 0
while i < n_symbols:
    password = password + symbols[random.randint(0,len(symbols)-1)]
    i +=1

i = 0
while i < n_numbers:
    password = password + numbers[random.randint(0,len(numbers)-1)]
    i +=1

print(f"Original string: {password}")

str_var = list(password)
random.shuffle(str_var)
password = ''.join(str_var)
print(f"Shuffled string: {password}")
