try:
    file = open("D30_exceptions-JSON/afile.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("D30_exceptions-JSON/afile.txt", "w")
    print("File doesnt exists. Creating now")
    file.write(f"Something")
except KeyError as error_message:
    print(f"the key {error_message} is not valid")
else:
    content = file.read()
    print(content)
finally:
    # raise TypeError("This is a made up error")
    print("ok")
