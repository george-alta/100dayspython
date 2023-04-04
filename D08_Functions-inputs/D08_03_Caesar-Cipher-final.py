from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar (original_message, shift_amount, cipher_direction):
    shift_amount = shift_amount % 26
    output = ""
    for char in original_message:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode": new_position = (position + shift_amount)%26
            elif cipher_direction == "decode": new_position = (position - shift_amount)
            output += alphabet[new_position]
        else:
            output += char
    print(f"the {cipher_direction}d text is '{output}'")
    return(output)

print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode' or direction == 'decode':
        caesar(text,shift,direction)
    else:
        print("please enter valid commands")
    if (input("Do you want to run this again? yes/no ").lower() == "no"): 
        print("Goodbye")
        break

