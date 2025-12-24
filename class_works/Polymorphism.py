#Types of Polymorphism
#method overloading
#method overriding
#operator overloading

#Method overloading
class Hotstar:
    def playvideo(self,username):
        print("Movie with Ads")
        print("Limited access for movies")
        print("Quality is limited")
        print("One device logic")
        print("No download option")
        print("No live access")
        print("Sound Quality reduces")

    def playvideo(self,premimum):
        print("Movie without Ads")
        print("Unlimited access for movies")
        print("High Quality")
        print("Multiple device logic")
        print("Download option is available")
        print("Live access")
        print("Improved Sound Quality")

sathish = Hotstar()
sathish.playvideo("Sathish")


#Method Overriding

class Hotstar:
    def __init__(self,username):
        print(f"Hi {username} Welcome to the Hotstar".center(40,'-'))
    def playvideo(self):
        print("Movie with Ads")
        print("Limited access for movies")
        print("Quality is limited")
        print("One device logic")
        print("No download option")
        print("No live access")
        print("Sound Quality reduces")
    def login(self):
        print("Login is same")
    def interface(self):
        print("Same interface")
    def profile(self):
        print("Profile is same")

class PremimumUser(Hotstar):
    def __init__(self,username):
        print(f"Hi {username} Welcome to the Hotstar.Enjoy the premimum".center(60,'-'))
    def playvideo(self):
        print("Movie without Ads")
        print("Unlimited access for movies")
        print("High Quality")
        print("Multiple device logic")
        print("Download option is available")
        print("Live access")
        print("Improved Sound Quality")

sathish = Hotstar("Sathish")
sathish.playvideo()
sathish.login()

randheer = PremimumUser("Randheer")
randheer.playvideo()
randheer.login()


class Instagram:
    def feed(self):
        print("Feed is same for all")
    def scrolling(self):
        print("Scrolling is same for all")
    def share(self):
        print("Share is same for all")
    def like(self):
        print("like is same for all")
    def repost(self):
        print("repost is same for all")
    def comment(self):
        print("comment is same for all")
    def profile(self):
        print("No Professional dashboard")
    def posting(self):
        print("No insights are available")
        
            
class Creator(Instagram):
    def profile(self):
        print("Professional dashboard is adding in that grid")

    def post(self):
        print("You can see the reach, profile activites, followers")
        

krishna = Creator()
krishna.profile()
krishna.posting()

sumanth = Instagram()             
sumanth.profile()
sumanth.posting()


#Operator Overloading

class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        return self.num+other.num

n1= Number(10)
n2= Number(20)

print(n1+n2)


























