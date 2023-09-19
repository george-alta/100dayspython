"""print("Hello"[4])
print("123"+"456")

print(123+456)
print(123_345_312)
print(3.1415)

print(True)
"""
# data types
# boolean, int, float, string...

num_char = len(input("what is your name?"))
num_char_str = str(num_char)
# print("your name has "+ num_char +" characters") // this is an error, because num_char is int
print(type(num_char))
print(type(num_char_str))
print("your name has "+ num_char_str +" characters") 