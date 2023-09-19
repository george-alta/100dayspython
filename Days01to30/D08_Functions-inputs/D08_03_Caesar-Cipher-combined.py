abc = 'abcdefghijklmnopqrstuvwxyz' #26 char
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar (original_message, shift_amount, cipher_direction):
    shift_amount = shift_amount % 26
    output = ""
    for letter in original_message:
        position = alphabet.index(letter)
        if cipher_direction == "encode": new_position = (position + shift_amount)%26
        elif cipher_direction == "decode": new_position = (position - shift_amount)
        output += alphabet[new_position]
    print(f"the {cipher_direction}d text is '{output}'")
    return(output)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode' or direction == 'decode':
        caesar(text,shift,direction)
    else:
        print("enter valid commands")

