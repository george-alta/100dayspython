abc = 'abcdefghijklmnopqrstuvwxyz' #26 char
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(message, step):
    step = step % 26
    output = "" #for the list function
    for letter in message:

        position = alphabet.index(letter)
        new_position = (position + step)%26
        result += alphabet[new_position]
    return (f"{output}")

def decode(message, step):
    step = step % 26
    output = ""
    for letter in message:
        position= alphabet.index(letter)
        new_position = position - step
        output += alphabet[new_position]
    return output

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        print(encode(text, shift))
    elif direction=="decode":
        print(decode(text, shift))
    else:
        print("enter a valid command")