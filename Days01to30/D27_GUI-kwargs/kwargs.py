def calculate(n, **kwargs):
    print(kwargs)

    for key, value in kwargs.items():
        print(key)
        print(value)

    print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)
    pass


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(model="GT-R", make="Nissan")
print(my_car.model)

my_other_car = Car(model="Estima")
print(my_other_car.make)

# *args are collected as a tuple
# **kwargs are collected as dictionary
