print("welcome to the rollercoaster")
height = int(input("please enter your height in cms: "))
if height < 120:
    print ("you are not tall enough to ride the rollercoaster 😭")
else:
    print("welcome aboard 😄")
    age = int(input("what is your age? "))
    if age < 12:
        print("please pay $5.")
    elif age >= 12 and age <= 18:
        print("please pay $7.")
    else:
        print("please pay $12.")