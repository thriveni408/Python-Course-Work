
1.
import math

circle_geometry= lambda r: (round(math.pi*r*r,2),round(2*math.pi*r,2))

print(circle_geometry(7))
print(circle_geometry(2.5))


2.
import random
def pick_random_team(members, team_size):
    print(random.choices(members,k=team_size))

pick_random_team(["Alice", "Bob", "Charlie", "David"], 2)
pick_random_team(["A", "B", "C", "D", "E"], 3)


3.
temp=[36, 42, 39, 45, 41]
res= list(filter(lambda i:i>40,temp))
print(res)


4.
def is_prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True



def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)


        
n=int(input("Enter the number: "))
print(is_prime(n))


5.
def reverse_number(n):
    if n==0:
        return 
    print(n%10,end='')
    return reverse_number(n//10)




def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)


reverse_number(12398765434)


6.
inp=["cat", "car", "bat", "apple"]
ch='c'
res= list(filter(lambda i: i.startswith(ch),inp))

print(res)


7.
#string_utils.py
def is_palindrome(word):
    if word== word[::-1]:
        return True
    else:
        return False

def capitalize_words(text):
    return text.capitalize()


#main.py
#from string_utils import is_palindrome,capitalize_words
print(is_palindrome("madam"))
print(capitalize_words("hello world"))


8.
words=["Apple", "apple", "Banana", "BANANA", "Cherry"]
res= set(map(lambda i : i.lower(),words))
print(res)


9.
def countdown(n):
    for i in range(n,-1,-1):
        yield i

n=int(input())
c=countdown(n)
for i in range(n+1):
    print(next(c))


10.
def nested_sum(n):
    total = 0
    for item in lst:
        if type(item) == list:
            total += nested_sum(item)
        else:
            total += item
    return total


nested_sum([[1, 2], [3, [4, 5]]])
