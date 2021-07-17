class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1

    def print_info(self):
        print(f"\nID = {self.id}")
        print(f"username = {self.username}")
        print(f"followers = {self.followers}")
        print(f"following = {self.following}")


user1 = User("001", "user001")
user2 = User("002", "user002")

user1.follow(user2)

user1.print_info()
user2.print_info()
