# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

concat = (name1 + name2).lower()
number1 = concat.count("t") + concat.count("r") + concat.count("u") + concat.count("e")
number2 = concat.count("l") + concat.count("o") + concat.count("v") + concat.count("e")
score = number1 * 10 + number2

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")