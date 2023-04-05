print("welcome to the silent auction")
offer_book = {}
i = 0
highbid = 0
while True:
    cur_name = input("please enter your name: ")
    cur_offer = int(input("please enter your offer: "))
    offer_book[cur_name]=cur_offer
    i += 1
    if cur_offer > highbid: highbid = cur_offer

    if input("do you want to add another offer? yes/no: ") == "no":
        break

# print(offer_book)
winner = list(offer_book.keys())[list(offer_book.values()).index(highbid)]
print(f"total offers: {i}. The highest bid was {highbid}. The winner is '{winner.upper()}' 😄")  # prints winner

# to do. what if there is a tie.
# try catch int