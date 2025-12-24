#single Inheritance

class Whatsapp_v1:
    def messaging(self):
        print("You can message")
    def sharepics(self):
        print("You can share the photos")

imran = Whatsapp_v1()
print("Imran-v1")
imran.messaging()
imran.sharepics()

        
class Whatsapp_v2(Whatsapp_v1):
    def status(self):
        print("You can upload the status")
    def videos(self):
        print("You can send videos also")

santhosh = Whatsapp_v2()
print("santhosh-v2")
santhosh.status()
santhosh.videos()

#Multilevel Inheritance

class Whatsapp_v3(Whatsapp_v2):
    def calls(self):
        print("You can do video and audio calls")
    def groups(self):
        print("You can create a groups")

harsha = Whatsapp_v3()
print("harsha-v3")
harsha.messaging()
harsha.sharepics()
harsha.status()
harsha.videos()
harsha.calls()
harsha.groups()

#Multiple Inheritance

class Community:
    def clubgroup(self):
        print("You can create a community with clubing the group")
class Meta:
    def ai(self):
        print("You can chat, generate images and generate videos")
class Whatsapp_v4(Whatsapp_v3,Community,Meta):
    def channel(self):
        print("You can create channel to engage with your following")

randheer = Whatsapp_v4()
print("randheer-v4")
randheer.messaging()
randheer.sharepics()
randheer.status()
randheer.videos()
randheer.calls()
randheer.groups()
randheer.clubgroup()
randheer.ai()
randheer.channel()

#Hybrid Inheritance

#Hierarchical Inheritance

class Community:
    def clubgroup(self):
        print("You can create a community with clubing the group")
class Meta:
    def chat(self):
        print("You can chat")

class Meta1(Meta):
    def ai_images(self):
        print("You can generate images")
class Meta2(Meta):
    def human_emotions(self):
        print("You can share your feelings")
        
class Meta3(Meta1, Meta2):
    def technical(self):
        print("You can ask technical Questions also.Meta can provide all kind of things")

class Whatsapp_v4(Whatsapp_v3,Community,Meta3):
    def channel(self):
        print("You can create channel to engage with your following")

randheer = Whatsapp_v4()
print("randheer-v4")
randheer.messaging()
randheer.sharepics()
randheer.status()
randheer.videos()
randheer.calls()
randheer.groups()
randheer.clubgroup()
randheer.channel()
randheer.chat()
randheer.ai_images()
randheer.human_emotions()
randheer.technical()

















        





