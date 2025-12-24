class Instagram:
    def __init__(self, username, pwd):
        print("Welcome to the Instagram. Have Fun!!!")
        self.username = username
        self.__password = pwd      # private variable
        self._post = []            # protected variable

    # Getter
    def getPassword(self):
        return self.__password

    # Setter
    def setPassword(self, newPassword):
        self.__password = newPassword
        print("Password Updated")

    # Property (getter)
    @property
    def viewPost(self):
        return self._post

    # Property (setter)
    @viewPost.setter
    def viewPost(self, post):
        self._post.append(post)


# Object creation
randheer = Instagram("Randheer", "r@123")

# Instance variable change
print(f"Before: {randheer.username}")
randheer.username = "Sumanth"
print(f"After: {randheer.username}")

# Using property
print(randheer.viewPost)
randheer.viewPost = "hello"
randheer.viewPost = "First Reel"
print(randheer.viewPost)
