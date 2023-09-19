import random

word_list = ["ardvark", "baboon", "camel"]

# select random word

# secret_word = word_list[random.randint(0,len(word_list)-1)] this was the previous method
chosen_word = random.choice(word_list)

"""while True:
    guess = input("guess an animal: ").lower()
    if guess == chosen_word:
        print ("correct 😄")
        break
    else:
        print ("wrong")"""

guess = input("guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")