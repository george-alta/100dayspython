for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: # was an 'or' instead of 'ar'
    print("FizzBuzz")
  elif number % 3 == 0: #'elif' was added
    print("Fizz")
  elif number % 5 == 0: #'elif' was added
    print("Buzz")
  else:
    print([number])