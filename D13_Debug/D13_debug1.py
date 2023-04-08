############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21): # originally was 20, but range is [a,b), so to print i==20, range needs to be up to 21
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) #the original randit was (1,6). since the list goes from 0 to 5, needs to be adjusted
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year <= 1994: # added the = for include 1994
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you? ")) # added the 'int' command
# if age >= 18:
#     print(f"You can drive at age {age}.") # was not indented. was not as F string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # replaced the == for =. The == returns true or false. false == 0, so the next multiplication will be 0
# total_words = pages * word_per_page
# ## a good tip if things are playing funny is to use the print command to see where the variables are breaking.
# print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])