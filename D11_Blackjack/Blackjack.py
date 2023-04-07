############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def drawcard():
    return cards[random.randint(0,12)]
player_score = 0
computer_score = 0

def computer_play(hand):
    while sum(hand) < 17:
        hand.append(drawcard())
    return hand

def ace_in_hand(hand):
    for card in range(len(hand)):
        if hand[card] == 11:
            return(True)
    return False

def replace_ace(hand):
    for card in range(len(hand)):
        if hand[card] == 11:
            hand[card] = 1
            break
    return (hand)

while True:
    os.system("cls")
    print(logo)
    player_hand = []
    computer_hand = []
    print (f"             ")
    player_hand = [drawcard(),drawcard()]
    computer_hand = [drawcard(),drawcard()]
    player_lose = False

    print(f"Your Hand: {player_hand} - Total {sum(player_hand)}.")
    print(f"Computer Hand: [{computer_hand[0]} , _ ] \n\n")
    
    while True:
        if sum(player_hand) == 21:
            player_score += 1
            print(f"BLACKJACK! you win 😄. Current Score: {player_score} Human. {computer_score} CPU.")
            break
        next_play = input(f"Do you want to (d)raw another card or (s)tay? d/s: ")
        if next_play == "d":
            player_hand.append(drawcard())
            if sum(player_hand)>21 and ace_in_hand(player_hand):
                replace_ace(player_hand)
            elif sum(player_hand)>21 and not ace_in_hand(player_hand):
                computer_score += 1
                player_lose = True
                print(f"You lose: {sum(player_hand)} points 😭. Current Score: {player_score} Human. {computer_score} CPU.\n\n")
                break
            print(f"\nYour Hand: {player_hand} - Total {sum(player_hand)}.\n")
        if next_play == "s":
            break
    if not player_lose: # if player loses before this point, this code shouldn't be executed
        player_sum = sum(player_hand)
        computer_hand = computer_play(computer_hand)
        computer_sum = sum(computer_hand)
        print(f"\n --> Computer hand: {computer_hand}. Total {computer_sum}")
        print(f" --> Human hand: {player_hand}. Total {player_sum}\n")
        if computer_sum > 21 or computer_sum < player_sum:
            player_score +=1
            print (f"Computer loses 😄. Current Score: {player_score} Human. {computer_score} CPU.\n\n")
        elif computer_sum == player_sum:
            print(f"It's a draw at {player_sum} points. Current Score: {player_score} Human. {computer_score} CPU.\n\n")
        else:
            computer_score += 1
            print(f"computer wins 😭. Current Score: {player_score} Human. {computer_score} CPU.\n\n")


    if input("do you want to play again? y/n: ") == "n": break

print(f"End of game. Final score: {player_score} Human. {computer_score} CPU")

## TODO replace when there is an ace and score is over 21