# for number in range (a,b)
for number in range (1, 11): #prints 1 to 11, steps of 1
    print (number)

for number in range (1, 11, 3): #prints 1 to 11, steps of 3
    print (number)

#sum number from 1 to 100
total = 0 
for number in range (1, 101):
    total = total + number
print(f"the sum of number from 1 to 100 is {total}")
