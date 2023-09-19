# def add(*args):  # this can take any number of arguments
#     for n in args:
#         print(n)


def add(*args):  # this can take any number of arguments
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(45, 3, 2, 1, 54, 6, 7, 8, 5, 3)
