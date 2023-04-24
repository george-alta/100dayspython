# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"


with open("D24_File-IO/mail-merge/Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines(33)
    # names =
    names = [i.replace('\n', '') for i in names]

print(names)

with open("D24_File-IO/mail-merge/Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"D24_File-IO/mail-merge/Output/ReadyToSend/{stripped_name}.txt", mode="w+") as newletter:
            newletter.write(new_letter)
    # letter = [i.replace('\n', '') for i in letter]

# print(letter)
# for person in names:
#     with open(f"D24_File-IO/mail-merge/Output/ReadyToSend/{person}.txt", mode="w+") as newletter:
#         for line in letter:
#             thisline = line.replace(PLACEHOLDER, person)
#             newletter.write(f"{thisline}\n")
