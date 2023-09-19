from data import nato
"""
word = input("enter a word: ").upper()
spell = [nato[letter] for letter in word]
print(spell)

"""
# 1 line version
print([nato[letter] for letter in input("enter a word: ").upper()])
