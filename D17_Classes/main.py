class User:  # Every class must have first letter capitalised (PascalCase)
    # we need to establish the constructor
    def __init__(self, user_id, username):
        # init function is called every time a new object is created
        # next to self, we can add attributes
        self.id = user_id
        self.username = username
        # we can define starting variables, that we can later change
        self.followers = 0
        self.following = 0

    def follow(self, user):
        # if I follow another user, their count of followers count goes up by 1.
        # and the count of users I am following goes up by 1 as well
        user.followers += 1
        self.following += 1


user_1 = User("001", "Angela")  #
user_2 = User("002", "John")
# user_1.id = "001" #attributes ... not relevant anymore
# user_1.username = "John" .. not relevant anymore

user_1.follow(user_2)
# the constructor will define how many arguments we need to send to create the object

print(user_1.id)
print(user_1.username)
print(user_1.following)
# we can change attribute values later on: user_1.followers = 55
print(user_2.followers)
