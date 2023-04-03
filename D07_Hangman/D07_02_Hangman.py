import random
word_list = ["ardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= ''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========= ''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= ''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========= ''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========= ''', '''
  +---+
  |   |
  O   |
      |
      |
      |
========= ''', ''' 
  +---+
  |   |
      |
      |
      |
      |
========= ''']

# select random word
chosen_word = random.choice(word_list)
display = []
# create the list with _
for n in range (len(chosen_word)):
    display.append("_")

print (f"\n{' '.join(display)}\n")

lives = 6
left_to_guess = len(chosen_word)
this_guess = 0

while lives > 0 and left_to_guess > 0:

    guess = input("guess a letter: ").lower()
    this_guess = 0
    #prevent double input of the same letter
    if guess in display:
        print("you already selected this letter")
        continue

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            left_to_guess -= 1

    if guess not in chosen_word: #all guesses were wrong in this round
        lives -= 1
        if lives == 1: print(f"{stages[lives]}{lives} life left")
        else: print(f"{stages[lives]}{lives} lives left")
    print (f"\n{' '.join(display)}\n")

if(lives) == 0: print(f"No lives left. game over 😭. the magic word was '{chosen_word}'")
if(left_to_guess)== 0: print(f"you won 😄. the magic word was '{chosen_word}'")