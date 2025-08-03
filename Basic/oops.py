# class Car:
#     def __init__(self,brand,model,year):  #__init__ is a special method in python classes, All classes have a special method called __init__ which is automatically called when an object of that class is created
#         self.brand= brand                 # self para is a reference to the current instance of the class and is used to access variables and methods from the class
#         self.model = model
#         self.year = year

#     def display(self):
#         print(f"Name:{self.brand}, model:{self.model},year:{self.year}")

    
# s1 = Car("Creta",23,2025)
# s1.display()

# class Student:
#     def __init__(self,name,phy,eng,math):
#         self.name = name
#         self.phy = phy
#         self.eng = eng
#         self.math = math

#     def print(self):
#         print(f"Name:{self.name}, phy:{self.phy}, eng:{self.eng}, math:{self.math}")
#         return (self.phy + self.eng + self.math)/3
    

# s1 = Student("Madhavi", 97,90,85)
# print(s1.print())


# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.


# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def getAvg(self):
#         sum = 0
#         for i in self.marks:
#             sum+=i
#         print(self.name,"Your avg is",sum/len(self.marks))

# s1 = Student("Madhavi", [97,99,98])
# print(s1.getAvg())

# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal,acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount,"was debited")
        print("total balance = ", self.print_balance())

    # Credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount,"is credited")
        print("total balance = ", self.print_balance())

    # printing the balance
    def print_balance(self):
        return self.balance
        

acc1 = Account(35000, 123)
print(acc1.debit(1000))
print(acc1.credit(500))
print(acc1.print_balance())