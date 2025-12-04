# 1. Automated Salary Tax Calculator 
sal = int(input("Enter the sal: "))
tax=0

if sal<=250000:
    tax=0
elif 250000<sal<=500000:
    tax=sal*0.05
elif 500000<sal<=1000000:
    tax=sal*0.2
elif sal>1000000:
    tax=sal*0.3
print(f'Tax amount: {tax}\nSalary after tax: {sal-tax}')


# 2. Movie Ticket Pricing System 
n=int(input("No of persons: "))
cost=0
for i in range(n):
    age=int(input("Enter the age: "))
    if age<5:
        continue
    elif 5<=age<=18:
        cost+=100
    elif 19<=age<=60:
        cost+=150
    elif age>60:
        cost+=120
print(cost)


# 3. Electricity Bill Generator 
units=int(input("Enter the units: "))
price=0
if units<=100:
    price=units*1.5
elif 100<units<=200:
    price=150+(units-100)*2.5
elif 200<units<=500:
    price=400+(units-200)*4
elif units>500:
    price=1600+(units-500)*6
print(price)


# 4. Car Parking Fee Calculator Charges are based on hours parked: 
hrs=int(input("Enter the hours: "))
fee=0
if hrs<=2:
    fee=30
elif 2<hrs<24:
    fee=30+(hrs-2)*10
elif hrs==24:
    fee=200
print(fee)


# 5. Product Inventory Checker (Nested Conditionals) 
name=input("Enter the name: ")
qua=int(input("Enter the qua: "))
if qua==0:
    print(f'{name}: Out of Stock')
elif 0<qua<=10:
    print(f'{name}: Low Stock')
elif 10<qua<=50:
    print(f'{name}:  In Stock')
elif qua>50:
    print(f'{name}:  Overstocked')


# 6. Pattern – Row-wise Alternating 0 and 1 (Nested Loops) 
n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        print((i+j)%2,end=' ')
    print()


# 7. Gym Subscription Billing (Menu Driven Program) Menu: 
billing={1:500,2:1300,3:5000}
ch=int(input("Enter the choice: "))
n=int(input("No of ppl: "))
print(billing[ch]*n)


# 8. Billing Bot – Apply Discount Based on Amount 
amount=float(input("Enter the amount: "))
discount=0
if 0<=amount<1000:
    discount=0
elif 1000<=amount<5000:
    discount=amount*0.05
elif 5000<=amount<10000:
    discount=amount*0.1
elif amount>10000:
    discount=amount*0.15

print(amount-discount)


# 9 : ATM PIN Verification with Blocking Logic 
str_pin=1234
for i in range(3):
    pin=int(input("Enter the pin: "))
    if pin==str_pin:
        print("Access Granted")
        break
else:
    print("ATM Blocked. Try Again Later.")


# 10 : Bus Booking System 
n=int(input("Enter the no of seats: "))
bs= tuple(map(int,input().split()))
print(f'Total Seats: {n}\nBooked: {len(bs)}\nAvailable: {n-len(bs)}')

