import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

print(logo)
chosen_word = random.choice(word_list) # select random word
display = []
for n in range (len(chosen_word)): # create the list with _
    display.append("_")

print (f"\n{' '.join(display)}\n")

lives = 6
left_to_guess = len(chosen_word)

while lives > 0 and left_to_guess > 0: #games ends if no letters left to guess or no lives left

    guess = input("guess a letter: ").lower()
    
    if guess in display: #prevent double input of the same letter
        print("you already selected this letter")
        continue

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            left_to_guess -= 1

    if guess not in chosen_word: # all guesses were wrong in this round
        lives -= 1
        if lives == 1: print(f"{stages[lives]} '{guess}' was not in the secret word. Now you have {lives} life left")
        else: print(f"{stages[lives]} '{guess}' was not in the secret word. Now you have {lives} lives left")
    print (f"\n{' '.join(display)}\n") 

if(lives) == 0: print(f"No lives left. game over 😭. the magic word was '{chosen_word}'")
if(left_to_guess)== 0: print(f"you won 😄. the magic word was '{chosen_word}'")