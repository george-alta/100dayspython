def encode(message, step):
    step = step % 26
    abc = 'abcdefghijklmnopqrstuvwxyz' #26 char
    output = ""
    for letter in message:
        pos1 = abc.find(letter)
        pos2 = (pos1 + step) % 26
        #if pos2 > 25:
        #   pos2 -= 25
        # print(f"{pos1} becomes {pos2}")
        output = output + abc[pos2]
    # print(f"{message} {step}: {output}")
    return (f"{output}")

### solo falta cuando el decoder se tiene que devolver desde 26
def decode(message, step):
    step = step % 26
    abc = 'abcdefghijklmnopqrstuvwxyz' #26 char
    output = ""
    for letter in message:
        pos2 = abc.find(letter)
        if (pos2 - step) >= 0:
            pos1 = (pos2 - step)
        else: 
            pos1 = (26+(pos2 - step))%26
        #if pos2 > 25:
        #   pos2 -= 25
        # print(f"{step}: {pos2} becomes {pos1}")
        output = output + abc[pos1]
    return output

print(f'encode 17 {encode("holas",17)}')
print(f'decode 17 {decode(encode("holas",17),17)}')

print(f'encode 35 {encode("holas",35)}')
print(f'decode 35 {decode(encode("holas",35),35)}')

print(f'encode 88 {encode("holas",88)}')
print(f'decode 88 {decode(encode("holas",88),88)}')

print(f'encode 5 {encode("holas",5)}')
print(f'decode 5 {decode(encode("holas",5),5)}')

print(f'encode 10 {encode("holas",10)}')
print(f'decode 10 {decode(encode("holas",10),10)}')

print(f'encode 4 {encode("holas",4)}')
print(f'decode 4 {decode(encode("holas",4),4)}')
