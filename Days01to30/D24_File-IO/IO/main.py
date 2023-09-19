
# To open a file
# with open("D24_File-IO\IO\my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# to edit a file w: write, a: append
with open("D24_File-IO\IO\my_file.txt", mode="a") as file:
    file.write("\nnew appended text")
