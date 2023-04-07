import random
import os
from art import logo

times_run = 0
win_count = 0

def guess(number,secret,lives):
    global win_count
    if number == secret:
        print(f"💎💎You guessed it!  💎💎 the secret number was {number}\n")
        result = "win"
        win_count += 1
    elif number < secret:
        lives -= 1
        print(f"⏫ Aim higher ⏫ You have {lives} lives left.\n")
        result = "low"
    else:
        lives -= 1
        print(f"⏬ Aim Lower ⏬ You have {lives} lives left.\n")
        result = "high"
    return [result, lives]

def play():
    os.system("cls")
    print(logo)
    global times_run
    times_run += 1
    secret = random.randint(0,100)
    print("welcome to number guesser.")
    difficulty = input("please choose difficulty: easy/hard ").lower()
    if difficulty == "hard":
        lives = 5
    elif difficulty == "easy":
        lives = 10
    
    while lives > 0:
        guess_attempt = int(input("\nGuess a number 1 to 100: "))
        run_result = guess(number=guess_attempt,secret=secret,lives=lives)
        lives = run_result[1]
        if run_result[0] == "win": 
            return
    if lives == 0: 
        print("you ran out of lives 😭😭😭😭")
        return

game_ended = False

while not game_ended:
    play()
    question = input(f"Total games: {times_run}. Total wins: {win_count}. Do you want to play again? y/n: ").lower()
    if question == "n":
        print(f"Game ending now. {round(win_count/times_run*100,2)}% times won")
        game_ended = True