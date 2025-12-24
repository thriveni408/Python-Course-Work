class Instagram:
    # Class attribute
    settings = ['Ins', 'Sta', 'Pri']

    # Constructor
    def __init__(self, username, password, bio=''):
        self.username = username
        self.password = password
        self.bio = bio

    # Instance method
    def userdetails(self):
        print(f"Hello {self.username}")
        print(f"Bio: {self.bio}")

    # Class method
    @classmethod
    def settingsupdate(cls):
        print("Settings:", cls.settings)

    # Static method
    @staticmethod
    def welcome():
        print("Welcome to Instagram. Have Fun!!")


# Creating object (instance)
randheer = Instagram("Randheer", "r@123", "Python Learner")

# Accessing instance attributes
print(randheer.username)
print(randheer.password)
print(randheer.bio)

# Accessing class attribute
print(randheer.settings)
print(Instagram.settings)

# Calling methods
randheer.userdetails()

randheer.settingsupdate()
Instagram.settingsupdate()

randheer.welcome()
Instagram.welcome()
