#Create student class that takes names and marks of three subjects as arguments in constructor.Then create a method to print the average.
"""class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        avg=(self.marks1+self.marks2+self.marks3)/3
        print("The average of the marks of three subjects is:",avg)
name= input("Enter the name of the student:")
marks1= float(input("Enter the marks of subject 1:"))
marks2= float(input("Enter the marks of subject 2:"))
marks3= float(input("Enter the marks of subject 3:"))
student1=Student(name,marks1,marks2,marks3)
student1.average()"""

#Create Account class with two attributes-balance and account number.Create methods for debit, credit and printing the balance.
class Account:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance

    def debit(self, amount):
        self.balance-= amount

    def credit(self, amount):
        self.balance+= amount

    def print_balance(self):
        print("The balance of the account is:", self.balance)
account_no=input("Enter the account number:")
balance=float(input("Enter the balance of the account:"))
account1=Account(account_no, balance)
account1.print_balance()
amount=input("Enter the amount as a d or c:")
if amount=="d":
    amount=float(input("Enter the amount to debit:"))
    account1.debit(amount)
if amount=="c":
    amount=float(input("Enter the amount to credit:"))
    account1.credit(amount)
account1.print_balance()