import random
import os
from art import logo, vs
from gamedata import data


def select(num):
    """Returns [name, follower_count, description, country] for the given n"""
    result = [data[num]["name"],data[num]["follower_count"],data[num]["description"],data[num]["country"]]
    # print(result)
    return result

def compare(a,b,option):
    """Compares A & B and checks if the user choose correctly"""
    os.system("cls")
    if (option == "a" and a > b) or (option == "b" and b > a):
        print(f"A:{a} followers B:{b} followers. You Win😄😄😄")
        return True
    elif a ==b:
        print(f"A:{a} followers B:{b} followers. It's a Draw... you win this time😄😄😄")
        return True
    else:
        print(f"A:{a} followers B:{b} followers. You Lose 😭")
        return False

def play():
    os.system("cls")
    pool = len(data)-1
    score = 0
    game_finished = False
    first_run = True
    while not game_finished:
        
        print(logo)
        if not first_run: print(f"You Guessed it!. Current score: {score}")
        if first_run: charA = random.randint(0,pool)
        CompareA = select(charA)
        print(f"Compare A: {CompareA[0]}, a {CompareA[2]}, from {CompareA[3]}")
        charB = random.randint(0,pool)
        while charA == charB: ## to prevent duplication
            charB = random.randint(0,pool)
        CompareB = select(charB)
        print(f"{vs}")
        print(f"Against B: {CompareB[0]}, a {CompareB[2]}, from {CompareB[3]}")
        question = input("Who has more followers? type A or B:").lower()
        result = compare(a=CompareA[1], b=CompareB[1], option = question)
        if result: 
            score +=1
            charA = charB
            first_run = False
        else: game_finished = True
    return score

final_score = play()
print(f"\n--> Game over, your final score was: {final_score}")