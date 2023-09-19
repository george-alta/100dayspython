import os
from art import logo

print(logo)
print("                 Welcome to the silent auction\n\n")
bids = {}
bidding_finished = False
i = 0
highbid = 0
while not bidding_finished:
    cur_name = input("please enter your name: ")
    cur_offer = int(input("please enter your offer: "))
    bids[cur_name]=cur_offer
    i += 1
    if cur_offer > highbid: highbid = cur_offer
    os.system('cls')

    if input("do you want to add another offer? yes/no: ") == "no": bidding_finished = True

os.system('cls')

winner_list=[]
for people in bids:
    if highbid == bids[people]: winner_list.append(people)

if len(winner_list) == 1:
    print(f"total offers: {i}. \nThe highest bid was {highbid}. \n\nThe winner is '{winner_list[0]}' 😄\n\n")
else:
    print(f"total offers: {i}. \nThe highest bid was {highbid}. \n\nThere is a tie between: {', '.join(winner_list)} 🤔\n\n")
   
# winner = list(bids.keys())[list(bids.values()).index(highbid)]
# print(winner)
# print(f"total offers: {i}. \nThe highest bid was {highbid}. \n\nThe winner is '{winner.upper()}' 😄\n\n")  # prints winner
