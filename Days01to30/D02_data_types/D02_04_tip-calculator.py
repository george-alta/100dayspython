#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("welcome to tip calculator.")
bill = float(input("what was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
group = int(input("How Many people to split the bill? "))
split = round((bill / group) * (1 + tip/100), 2)
split = "{:.2f}".format(split)
print (f"Each pershon should pay: ${split}")