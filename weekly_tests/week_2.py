# 1.The Birthday Format Fixer (String & Type Conversion)
date=input("Enter the date: ").split('-')
print(f'{date[2]}/{date[1]}/{date[0]}')


#2.The Even Odd Game (Conditional Statement)
n=int(input("Enter the n:"))
if n%2==0:
    print("Even Winner")
else:
    print("Odd Winner")


#3.Vowel Replacer Bot (String Methods)
s=input("Ente the string: ").lower()
s=s.replace('a','*')
s=s.replace('e','*')
s=s.replace('i','*')
s=s.replace('o','*')
s=s.replace('u','*')
print(s)

print(s.translate(str.maketrans('aeiou','*****')))


#4.Shopping Cart Analyzer (List Operations)
prices=list(map(float,input("Enter the prices: ").split()))
print(sum(prices))
print(max(prices))


#5.Secure Login System (Tuple & Conditional)
credentials = ("admin", "python123")
username=input("Enter the username: ")
password=input("Enter the password: ")

if (username,password)==credentials:
    print("Login valid")
else:
    print("Invalid Login")


#6.Remove Duplicates from Set (Set Operations)
names=input("Enter the names: ").split(',')
print(sorted(set(names)))


#7.Student Marks Record (Dictionary Operations)
data={}
n=int(input("Enter the n: "))
for i in range(n):
    name,mark= input().split()
    data[name]=int(mark)


name=None
max_marks=0

for i in data:
    if data[i]>max_marks:
        name=i
        max_marks=data[i]


print(name)


#8.Reverse My Words (String Slicing)
sen=input("Enter the sentence").split()
s=''
for i in sen:
    s+=i[::-1]+' '

print(s)


#9.Clean My List (List and Type Conversion)
nums=list(map(int,input().split()))

while 0 in nums:
    nums.remove(0)

print(nums)



#10.The Frequency Counter (Dictionary + String)
res=[]
for i in nums:
    if i!=0:
        res.append(i)
        
print(res)


sen=input()
res={}
for i in sen:
    if i!=' ':
        res[i]=sen.count(i)

print(res)