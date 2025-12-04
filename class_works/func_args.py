def status():
    course='Java'
    print("Beg:",course)
    def change():
        nonlocal course
        course='Python'
        print("In Btw:",course)

    change()
    print("Final:",course)


status()

name='sumanth'
def data():
    global name
    name='ruchitha'
    print("Inside:",name)

data()
print("Outside:",name)


def squares(**numbers):
    print(numbers)


squares(k1='1',k2='2',k3='3')
squares(k1='1',k2='2')
squares(k1='1',k2='2',k3='3',k4=4)
squares(k1='1',k2='2',k3='3',k4=4,k5=5)


def display(*names):
    print(names)


display('Ajay','krishna','ruchitha','varsha','preethi')
display('santhosh','harsha','satish')
display('rama','randheer','priya','praveen')
display('Imran','sumanth')
display('prasad')

def display(username,mail,pwd='1234'):
    print(f'Username: {username}\nMail:{mail}\nPassword:{pwd}')

uname=input("Enter the username: ")
mail=input("Enter the mail: ")
pwd=input("Enter the password: ")


display(uname,mail)
display(uname,mail,pwd)
display(username=uname,mail=mail,pwd=pwd)
display(pwd=pwd,username=uname,mail=mail)
display(username=uname,pwd=pwd,mail=mail)


display(uname,mail,pwd)
display(mail,uname,pwd)
display(pwd,uname,mail,)
display(uname,pwd,mail)
