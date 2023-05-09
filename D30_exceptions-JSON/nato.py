nato = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"}


def generate_phonetic():
    word = input("enter a word: ").upper()
    try:
        output_list = [nato[letter] for letter in word]
    except KeyError:
        # if a non valid character is entered, another prompt is created
        print("Enter only letters please")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
