# 1.Equvalint,scalable,iso
a,b,c = tuple(map(int,input("Enter the numbers:").split()))
if a==b and b==c and a==c:
    print("Equ")
elif a!=b and b!=c and a!=c:
    print("Sca")
else:
    print("Iso")


# 2.vowel,consonant,char
ch = input()
vowels = 'aeiouAEIOU'
if ch in vowels:
    print("Vowels")
elif ch.isalpha():
    print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("special char")


# 3. BMI Calculator and Category
h = float(input())
w = float(input())
bmi = w / (h*h)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


# 4.Electricity bill calculate
units = int(input("Enter the units consumed:"))
charge = 0
if units<=100:
    charge = units*1
elif 100<units<=200:
    charge = (100*1) + (units-100)*2
else:
    charge = (100*1) + (100*2) + (units-200)*3
print(charge)


# 5.amstrong numbers
num = input("Enter the  number : ")
res = 0
l = len(num)
for i in num:
    res += int(i)**l
if res ==int(num):
    print("Amstrong")
else:
    print("Not amstrong")

# 6.validate strong password
a = input("Enter the password:")
has_upper = False
has_lower = False
has_digit = False
for ch in a:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    if has_upper and has_lower and has_digit and len(a)>=8:
        print("Strong password")
        break
else:
    print("Weak password")


# 7. ATM withdrawal
balance,withdrawal = map(int,input("Enter the amount to withdraw:").split())
if withdrawal >=500 and withdrawal%100==0 and withdrawal<=balance:
    print("Successfully withdrawn")
else:
    print("Insufficient balance or invalid amount")


# 8.Ticket fare
age = int(input("Enter the age:"))
price = 100
fare = 0
if 5<=age<=18:
    fare = price - price*0.5
elif age>60:
    fare = price - price*0.3
else:
    fare = price
print(fare)


# 9. 24-hours to 12-hours format conversion
hrs,min = tuple(map(int,input("Enter time in 24-hours format: ").split(':')))
if 12<=hrs<=23:
    print(f'{hrs-12}:{min} PM')
elif 0<=hrs<12:
    print(f'{hrs}:{min} AM')


# 10.character based on ASCII value
ch = input("Enter the character:")
ascii_value = ord(ch)
if 48<=ascii_value<=57:
    print("Digit")
elif 65<=ascii_value<=90 or 97<=ascii_value<=122:
    print("Alphabet")
else:
    print("Special character")


# 11.Grading system with nested bands
marks = int(input("Enter the marks:"))
if 0<=marks<=100:
    if marks>=90:
        print("A")
    elif 85<=marks<90:
        print("B+")
    elif 80<=marks<85:
        print("B")
    elif 70<=marks<84:
        print("C")
    else:
        print("F")


# 12.currency denominations
amount = int(input("Enter the currency: "))
denominations= [2000,500,200,100,50,20,10,5,2,1]
result = []
for denom in denominations:
    if amount >=denom:
        count = amount//denom
        amount %= denom
        if count >0:
            result.append(f'{count}x{denom}')
output = ','.join(result)
print(f' -> Output:{output}')


# 13.movie ticket price
day = input("Enter the day: ")
age = int(input("Enter the age:"))
weekday = ['monday','tuesday','wednesday','thursday','friday']
weekend = ['saturday','sunday']
price = 0
day = day.lower()
if day in weekday:
    if 0<=age<=12:
        price= 150*0.5
    elif 13<=age<=60:
        price = 150
    else:
        print("Invalid age")
elif day in weekend:
    if 0<=age<=12:
        price = 200*0.5
    elif 13<=age<=60:
        price = 200
    else:
        print("Invalid age")
else:
    print("Invalid day")

print(f'Ticket price: {price}')


# 14.Classify angle as Acute,Right,Obtuse,Stright
angle = int(input("Enter the angle: "))
if 0<angle<90:
    print("Acute angle")
elif angle ==90:
    print("Right angle")
elif 90<angle<180:
    print("Obtuse angle")
elif angle ==180:
    print("Straight angle")
else:
    print("Invalid angle")


# 15.Grade college admission based on marks in 3 subjects
m1 = int(input())
m2 = int(input())
m3 = int(input())
avg = (m1 + m2 + m3) / 3
if avg > 90 and m1 > 70 and m2 > 70 and m3 > 70:
    print("Admitted")
elif avg > 80:
    print("Waitlisted")
else:
    print("Rejected")


# 16.prefect number or not
num = int(input("Enter the number: "))
sum_of_divisors = 0
for i in range(1,num//2+1):
    if num%i ==0:
        sum_of_divisors += i
        print(i,end=' ')
if sum_of_divisors == num:
    print(f'\n{num} is a perfect number')
else:
    print(f'\n{num} is not a perfect number')


# 17.Identify type of triangle by angles
a = int(input())
b = int(input())
c = int(input())
if a == 90 or b == 90 or c == 90:
    print("Right")
elif a < 90 and b < 90 and c < 90:
    print("Acute")
else:
    print("Obtuse")


#18.Convert marks (0–100) to 10-point GPA scale
m = int(input())
if m >= 91:
    print(10)
else:
    if m >= 81:
        print(9)
    else:
        if m >= 71:
            print(8)
        else:
            if m >= 61:
                print(7)
            else:
                print(6)


# 19.Check if four digits form a lucky number (sum of first two == last two)
num = input("Enter a 4-digit number: ")
n = len(num)
if n%2==0:
    l = list(map(int,num))
    if sum(l[:n//2]) == sum(l[n//2:]):
        print("Lucky number")
    else:
        print("Not a lucky number")
else:    
    print("Enter a valid 4-digit number")


#20.Car insurance premium based on age and experience
age = int(input())
exp = int(input())
if age < 25 and exp < 3:
    print("High Risk")
elif age > 25 and exp > 5:
    print("Low Risk")
else:
    print("Medium Risk")


#21.Ticket system for amusement park
age = int(input())
if age < 12:
    print(50)
elif age < 60:
    print(100)
else:
    print(60)


#22.Classify number as Single, Double, or Triple digit
n = int(input())
if n < 10:
    print("Single Digit")
elif n < 100:
    print("Double Digit")
else:
    print("Triple Digit")


# 23.Validate time input (HH:MM format)
hrs,mins = tuple(map(int,input("Enter the time in HH:MM format:").split(':')))
if 0<=hrs<24 and 0<=mins<60:
    print("Valid time")
else:
    print("Invalid time")


# 24.Weather categorization by temperature
t = int(input())
if t < 10:
    print("Very Cold")
elif t <= 20:
    print("Cold")
elif t <= 30:
    print("Warm")
else:
    print("Hot")


#25.Assign mobile plan based on usage
gb = float(input())
if gb < 1:
    print("Plan A")
elif gb < 5:
    print("Plan B")
else:
    print("Plan C")


# 26.Identify duplicate digits in a 3-digit number
num = input("Enter a 3-digit number: ")
if len(set(num)) == len(num):
    print("No duplicate digits")
else:
    print("Duplicate digits found")

# check only duplicate digits
num = input("Enter a digit number: ")
s = set()
for i in num:
    if i not in s:
        s.add(i)
    else:
        print(i)
print(len(num) - len(set(num)))


# 27.Weekday classifier (Input: 1-7, Output: Day type)
data = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
day_num = int(input("Enter a number (1-7): "))
if day_num in data:
    if 1<=day_num<=5:
        print(f"{data[day_num]} is a weekday.")
    else:
        print(f"{data[day_num]} is a weekend.") 


# 28.Student attendance eligibility (> 75% to write exam)
att = int(input())
tot = int(input())
per = (att / tot) * 100
if per >= 75:
    print("Eligible")
else:
    print("Not Eligible")


# 29.grades increasing and decreasing order
a,b,c = map(int,input("Enter the three numbers:").split())
if a<=b<=c:
    print("Increasing order")
elif a>=b>=c:
    print("Decreasing order")
else:
    print("Neither increasing nor decreasing order")


# 30.validate mobile number
num = input("Enter the number: ")
if len(num) ==10:
    if num.isdigit():
        sts = '6789'
        if num[0] in sts:
            print("Valid phone number")
        else:
            print("Number should start with 6,7,8,9")
    else:
        print("enter the digit properly")
else:
    print("Length needs to 10")