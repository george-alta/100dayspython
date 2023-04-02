import random
i = 0
score_human = 0
score_cpu = 0
play_again = True
# 1 rock - 2 paper - 3 scissors


while play_again:
    player = int(input("Select: \n1 - Rock\n2 - paper\n3 - Scissors\n1,2,3: "))
    cpu = random.randint(1, 3)
    print(f"player choose {player} - computer choose {cpu}")

    if player == cpu:
        print(f"is a draw. Current score: {score_cpu} CPU - {score_human} Human")
    elif (player == 1 and cpu == 3) or (player == 2 and cpu == 1) or (player == 3 and cpu == 2):
        score_human += 1
        print (f"human wins. Current score: {score_cpu} CPU - {score_human} Human")
    else:
        score_cpu += 1
        print (f"CPU wins. Current score: {score_cpu} CPU - {score_human} Human")

    question = input("do you want to play again? yes / no: ")
    if question == "no":
        play_again = False
        print (f"Final score: {score_cpu} CPU - {score_human} Human")


"""while i <100:
    print(random.randint(1, 3))
    i += 1"""