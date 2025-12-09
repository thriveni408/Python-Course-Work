#1.Calculate BMI
def calculate_bmi(weight_kg, height_m):
    print('%.2f'%(weight_kg / (height_m * height_m)))

calculate_bmi(70, 1.75)
calculate_bmi(90, 1.8)

          
def calculate_bmi(weight_kg, height_m):
    BMI=weight_kg / (height_m * height_m)
    print(round(BMI,2))
    

calculate_bmi(70, 1.75)
calculate_bmi(90, 1.8)

#2.Filter Even Numbers
def filter_even(numbers):
    res=[i for i in numbers if i%2==0]
    print(res)

filter_even([1, 2, 3, 4, 5, 6])
filter_even([11, 15, 21])


#3.Generate Multiplication Table

def generate_table(n):
    table=[i*n for i in range(1,11)]
    print(table)
generate_table(2)
generate_table(5)


#4.Check Anagram
def is_anagram(str1, str2):
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "Olelh"))
print(is_anagram("apple", "pale"))


#5.Count Word Occurences
def count_words(text):
    res={}
    for i in text.split():
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    print(res)

count_words("this is a test this is")
count_words("hello hello world")

#6.Simulate LRU Cache
def lru_cache(requests, size):
    cache=[]
    for i in requests:
        if i in cache:
            cache.remove(i)
            cache.insert(0,i)
        else:
            if len(cache)<size:
                cache.insert(0,i)

            else:
                cache.pop()
                cache.insert(0,i)

    print(cache)
lru_cache([1,2,3,2,4,1], 3)            
lru_cache([5,6,7,8], 2)            
lru_cache([1,2,3,1], 2)            


#7.Flatten 2D List
def flatten_matrix(matrix):
    res=[]
    for i in matrix:
        for j in i:
            res.append(j)
        print(res)

flatten_matrix([[1, 2], [3, 4]])
flatten_matrix([[5], [6, 7], [8]])

        
#8.Create Email Address

def create_email(first_name, last_name, domain):
    print(f'{first_name.lower()}.{last_name.lower()}@{domain.lower()}.com')

create_email("John", "Doe", "gmail")
create_email("ALICE", "Smith", "yahoo")


#9.Find All Factors of a Number
def get_factors(n):
    res=[]
    for i in range(1,n//2+1):
        if n%i==0:
            res.append(i)
    res.append(n)
    print(i)
            
get_factors(12)
get_factors(17)
get_factors(28)


#10.Format invoice Entry
def format_invoice(item, quantity, price):
    total = quantity * price
    print(f'{item} x{quantity} @${price}=${total}')

format_invoice("Pen", 3, 10)
format_invoice("Notebook", 2, 45)
   





















