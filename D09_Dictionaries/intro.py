# this is a dictionary

mydict = {"bug":"unexpected behaviour",
          "function":"a piece of code to easily call over and over again",
         }
# print(mydict)

# to get the definition of a bug
print(mydict)

# to add element
mydict["loop"] =  "action of doing something over and over again"

print(mydict)

# to wipe a dictionary --->    mydict = {}

#to edit an item

mydict["bug"] = "some piece of code that is acting funny"

print(mydict)

for key in mydict:
    print(key) # this will print all the keys
    print(mydict[key]) # this will print the value