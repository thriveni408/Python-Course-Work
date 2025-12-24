#Q1. Types of Methods – Instance, Class, Static

class Student:
    total_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total_students += 1


    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def get_total_students(cls):
        print(f"Total Students: {cls.total_students}")

    @staticmethod
    def is_eligible(age):
        return 18 <= age <= 30


s1 = Student("Arun", 20)
s2 = Student("Meena", 17)
s1.display()
Student.get_total_students()
print(Student.is_eligible(25))

#Q2. Constructor Usage

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price}")


b = Book("The Alchemist", "Paulo Coelho", 299)
b.display_info()

#Q3. Encapsulation – Public, Protected, Private

class Account:
    def __init__(self, account_holder, pin):
        self.account_holder = account_holder
        self._balance = 0
        self.__pin = pin

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, pin, amount):
        if pin == self.__pin:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrawn ₹{amount}")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid PIN")

    def show_balance(self):
        print(f"Available Balance: ₹{self._balance}")


acc = Account("Ravi", 1234)
acc.deposit(5000)
acc.withdraw(1234, 1500)
acc.show_balance()

#Q4. Multilevel Inheritance – Ride Booking System

class User:
    def login(self):
        print("User logged in")

class Rider(User):
    def book_ride(self):
        print("Ride booked successfully")

class Payment(Rider):
    def make_payment(self):
        print("Payment completed")


p = Payment()
p.login()
p.book_ride()
p.make_payment()

#Q5. Multiple Inheritance – Food Delivery App

class LocationService:
    def track_location(self):
        print("Current location tracked")

class OrderService:
    def place_order(self):
        print("Order placed successfully")

class DeliveryApp(LocationService, OrderService):
    def confirm_delivery(self):
        print("Delivery confirmed to your address")

app = DeliveryApp()
app.track_location()
app.place_order()
app.confirm_delivery()

#Q6. Hierarchical Inheritance

class Employee:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Employee Name: {self.name}")

class Manager(Employee):
    def manage_team(self):
        print("Managing team...")

class Developer(Employee):
    def write_code(self):
        print("Writing code...")


m = Manager("Vikram")
d = Developer("Anjali")
m.show_name()
m.manage_team()
d.show_name()
d.write_code()

#Q7. Using super()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}")


t = Teacher("Suma", 35, "Math")
t.show()

#Q8. Class Variables vs Instance Variables

class Company:
    company_name= 'TechCorp'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f'Company: {Company.company_name}\nEmployee: {self.name}, Salary: {self.salary}')


e1 = Company("Rahul", 50000)
e2 = Company("Neha", 60000)
e1.display()
e2.display()

#Q9. Class Method vs Static Method

class Exam:
    pass_mark = 40

    @classmethod
    def change_pass_mark(cls,new_mark):
        cls.pass_mark = new_mark

    @staticmethod
    def is_pass(score):
        return score >= Exam.pass_mark


Exam.change_pass_mark(50)
print(Exam.is_pass(45))
print(Exam.is_pass(55))

#Q10. Abstraction – Notification System

class Engine:
    def start_engine(self):
        print("Engine started")

class Car(Engine):
    def start_car(self):
        self.start_engine()
        print('Car is running')


car = Car()
car.start_car()