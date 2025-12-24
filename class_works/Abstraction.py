from abc import ABC, abstractmethod

class BankAccount(ABC):
    def checkbalance(self,username):
        self.username=username
        print(f"\n\nHi {self.username}!!!1\nDisplay the balance")
        
    @abstractmethod
    def deposit(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass
class CurrentAccount(BankAccount):
    def deposit(self):
        print("Any time deposit")
    def withdraw(self):
        print("No limits")
    
    
class SavingsAccount(BankAccount):
    def deposit(self):
        print("No limits for deposit")
    def withdraw(self):
        print("Limits per day")
        
    
class SalaryAccount(BankAccount):
    def deposit(self):
        print("Depoist once in a time")
    def withdraw(self):
        print("No limit,charges are applied")
        
    
class JointAccount(BankAccount):
    def deposit(self):
        print("2 of them can deposit")
    def withdraw(self):
        print("No limit,both can withdraw")
        pass
    
class PensionAccount(BankAccount):
    def deposit(self):
        print("Once in a month")
    def withdraw(self):
        print("20K per day")
        
    
class FixedDepositAccount(BankAccount):
    def deposit(self):
        print("One time deposit")
    def withdraw(self):
        print("Once in a year")
        
leela=CurrentAccount()
varsha=SavingsAccount()
sumanth=SalaryAccount()
vasuSekar=JointAccount()
satish=PensionAccount()
kavya=FixedDepositAccount()

leela.checkbalance("leela")
leela.deposit()
leela.withdraw()

varsha.checkbalance("varsha")
varsha.deposit()
varsha.withdraw()

sumanth.checkbalance("sumanth")
sumanth.deposit()
sumanth.withdraw()

vasuSekar.checkbalance("vasuSekar")
vasuSekar.deposit()
vasuSekar.withdraw()

satish.checkbalance("satish")
satish.deposit()
satish.withdraw()

kavya.checkbalance("kavya")
kavya.deposit()
kavya.withdraw()