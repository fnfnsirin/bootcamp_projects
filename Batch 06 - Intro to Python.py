# -*- coding: utf-8 -*-

# -- Sheet --

# # Intro to Python Programming


print("hello")

print("floor division (int) = ",10//3,"\n               float = ",10/3)

# # Core concept
# * variable
# * data types
# * data structures
# * function
# * control flow


#variable
my_name = "Fern"

#del var
del my_name

#Data types
print(type("Fern"),type(10),type(3.33),type(True))

#convert str to int
x = "100"
x = int(x)
print(x,type(x))

x_str = str(x)
print(type(x_str))

# ## Type Hint


name: str = "fern"
print(name)

age: int = 25
print(age)

gpa: float = 3.54
print(gpa)

catlover: bool = True
print(catlover)

# ## String Method
# Func ที่ถูกสร้างขึ้นมาสำหรับ class/type/object หนึ่งๆ


text = "my name is fern"

text = text.upper()
text = text.lower()
text

text = text.replace('fern','dodo')
print(text)

#generic func, str method
len(text)-text.count(" ")

#Capitalize first word to upper
text.title()

#list (vector in R)
list_of_words = text.split(" ")
list_of_words

#str.join()
sentence =" ".join(list_of_words)
sentence

#slicing information
word = "hello world"

#index start 0
word[0]    #h
word[-1]   #d
word[0:4]  #hell
word[6:]   #world

word.split(" ")[1]

programming = "Python"

#String Immutable Objects ประกาศแล้ว เปลี่ยนค่าไม่ได้
cython = "C"+programming[1:]
cython

# ## Data Structure
# * List `[]`
# * Tuple `()`
# * Dictionary `{key: value}`
# * Set `{}`


#list Mutable can change
shopping_items = ['egg','milk','bread','noodle']
shopping_items[0] = 'banana'
shopping_items

#ADD new items in right of LIST
shopping_items.append("jam")
print(shopping_items)
shopping_items.append("chocolate")
print(shopping_items)

#.pop() del items in LIST
shopping_items.pop(4)

shopping_items

shopping_items.count('banana')

#list.copy() deep copy

# list can contain anything
students =[
    ('toy',88),
    ('mary',95),
    ('john',90)
]

students[0][1]

x=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

x[0][2]

#tuple => immutable object
data = (1,2,3,"toy","data science",True)
type(data)

#cannot update value
#data[3]="Anna"
#TypeError: 'tuple' object does not support item assignment

#Dictionary refer to name_key MUTABLE
customer = {
    'first_name': 'kasidis',
    'nick_name': 'toy',
    "age": 34,
    "love_hamburger": True,
    "fav_movies": ['Thor','Dr.Strange']
}

customer['fav_movies'][0]

customer["age"] = 25

customer

customer["fav_movies"][0] = 'Thor Ragnarok'
customer

#new key in dic
customer['city'] = 'London'
customer

'city' in customer

'country' in customer

if 'country' not in customer:
    customer['country'] = "USA"

customer

#del key
del customer['country']
customer

#dic method
type(customer)

list(customer.keys())

list(customer.values())

list(customer.items()) #dic to list of tuple

#set of unique value
fruits = ['banana','banana','apple','apple','lemon']
print(len(set(fruits)),set(fruits))

unique_fruits = set(fruits)
unique_fruits.add("grape")
unique_fruits

#intersect (duplicate of friend and you)
fruits_friend = {'banana', 'orange', 'apple','durian'}
fruits_friend.intersection(unique_fruits)

fruits_friend.union(unique_fruits)

#f string template
fav_language = 'R'
template = f"Hello my name is {name} and I,m {age}, My favorite language is {fav_language}"
template

#create new function concept reuseable
def greeting(name: str) -> None:
    print(f"Hello {name}!")

greeting("Fern")

def add_two_nums(a: int,b: int) -> int:
    """
    input: two integer numbers
    output: sum of two numbers
    """
    return a+b

result = add_two_nums(5,10)
print(result)

#lambda func
def greeting():
    print('Hello!')

greeting = lambda name: print(f"Hello {name}")

greeting("Anna")

def cube(base,pow=3):
    return base**pow

cube(10)

# ## Control Flow
# ควบคุมพฤติกรรมของโปรแกรม
# * IF
# * for
# * while


# if
score = int(input("What's exam score: "))
if score >= 80:
    print("Passed")
else:
    print("Failed")

#get input form a user
#score = int(input("What's exam score: "))

def grading(score: int):
    if score >= 80:
        print("Distinction")
    elif score >= 50:
        print("Passed")
    else:
        print("Failed")

grading(55)

#for loop
shopping_list = ['egg','milk','bread']
new_list = [] #empty list
for i in shopping_list:
    #print(f"I have to buy {i.upper()}")
    new_list.append(i.upper())

new_list

#list comprehension
new_list = [i.upper() for i in shopping_list]

new_list

# if-else + for loop
scores = [95,90,75,79,82]
grades = []
for score in scores:
    if score >= 80:
        grades.append("Passed")
    else:
        grades.append("Failed")
print(grades)

# while loop while true do something
count = 0
while count<5:
    print("hello:",count)
    count+=1

age = 24
age+=1
age+=1
age/=2
age*=3
age-=20
print(age)

print(True and True)
print(True and False)
print(False and True)
print(False and False)

#multiple if-else
weather = 'sunny'
weekday = False
if weather == 'sunny' and weekday:
    print("Go to starbucks")
else:
    print("Stay home ")

#while loop
count=0
while True:
    print(count)
    count+=1
    if count == 10:
        print("Program Ends.")
        break

def breaker(n):
    count = 0
    while True:
        print(count)
        count+=1
        if count == n:
            print("Program Ends.")
            break

breaker(3)

# ## OOP
# Object Oriented Programming
# Cookie Cutter🍪


#สร้างแม่พิมพ์ แล้ววปั๊มน้องหมาขึ้นมาใหม่
class Dog:
    def __init__(self, d_name, d_age, color): #special method
        self.d_name = d_name
        self.d_age = d_age
        self.color = color
    def hello(self):
        print(f"Hi my name is {self.d_name}!")
    def get_older(self):
        self.d_age+=1
        print(f"I'm getting older one year. I'm now {self.d_age}")

dog1 = Dog("milo",2,'black')
dog2 = Dog("rambo", 3,'golden')
dog1.hello()
dog2.hello()
dog1.get_older()
dog2.get_older()

print(dog1.d_name,dog1.d_age,dog1.color)

class ATM:
    # double underscore => dunder
    def __init__(self, names, balance):
        self.names = names
        self.balance = balance 

    def check_balance(self):
        message = f"Account: {self.names}, Balance: {self.balance}"
        print(message)
    
    def deposit(self, money):
        self.balance += money 
        print(f"New Balance: {self.balance}")
        print("Deposit successfully.")
    
    def change_name(self, new_acc_name):
        self.names = new_acc_name 
        print(f"New Name: {self.names}")
        print("Your account name has been changed.")

scb = ATM("fern",500)

scb.check_balance()
scb.deposit(900)

scb.change_name('Sirinthip.nga')

ttb = ATM("john",15000)

ttb.deposit(5000)

#Homework 1 PAO YING CHUB PYTHON use input()
#ATM Class => at least 5 methods



# -- Homework- Intro to Python --

# # Intro to Python
# Sirinthip Ngamchaluay (Fern)


# Homework 1 **PAO YING CHUB**
# 
# Homework 2 **`(OOP)` ATM Class** at least 5 methods


# ## Pao Ying Chub (Rock Paper Scissers) ✊🤞✋


import random
choice = [0,1,2]
user_win = 0
bot_win = 0
tie = 0
count = 0
while count >=0:
    user_action = int(input("User choose 0,1,2 (rock[0], paper[1], scissors[2]): "))
    if user_action not in choice:
        print("Please enter 0,1,2 again!")
    else:
        bot_action = random.choice(choice)
        print(f"Bot choose 0,1,2 (rock[0], paper[1], scissors[2]): {bot_action}")
        if user_action == bot_action:
            print("Tie")
            tie+=1
        elif (user_action==0 and bot_action==2) or (user_action==1 and bot_action==0) or (user_action==2 and bot_action==1):
            print("User win!")
            user_win+=1
        else:
            print("Bot win!")
            bot_win+=1
        end_game = input("Do you want to play again? (y/n): ").lower()
        count+=1
        if end_game=='n':break
print(f"Number of Rounds Played: {count}")
print(f"User wins: {user_win}")
print(f"Bot wins: {bot_win}")
print(f"Tie: {tie}")
if user_win+tie > bot_win+tie:result='User win!'
elif bot_win+tie > user_win+tie:result='Bot win!'
else:'Tie'
print(f"Summarise the result of Rock Paper Scissers: {result}")

# ## `(OOP)` ATM Class *(at least 5 methods)*


class ATM:
    def __init__(self, names, balance: float, password: str):
        self.names = names
        self.balance = balance
        self.password = password
        
    def check_balance(self):
        message = f"Account: {self.names}, Balance: {self.balance} THB."
        print(message,"\n")
    def deposit(self, money: float):
        self.balance += money
        print(f"Deposit Amount of {money} THB.")
        print(f"New Balance: {self.balance} THB.")
        print("Deposit successfully.\n")
    def withdraw(self,money: float):
        self.balance-=money
        print(f"Withdrawal of {money} THB.")
        print(f"New Balance: {self.balance} THB.")
        print("Withdraw successfully.\n")
    def transfer(self,money: float,payee: str):
        self.balance-=money
        print(f"Transter to {payee}, {money} THB.")
        print(f"New Balance: {self.balance} THB.\n")
    def paybill(self,money: float,payee: str,fee: float):
        self.balance=self.balance-money-fee
        print(f"Paybill to {payee}, {money+fee} THB.")
        print(f"New Balance: {self.balance} THB.\n")
    def change_name(self, new_acc_name: str):
        self.names = new_acc_name
        print(f"New Name: {self.names}")
        print("Your account name has been changed.\n")
    def change_password(self, new_password: str):
        self.password = new_password
        print(f"New Password: {self.password}\nYour password has been changed.")


#Set constant value
customers = []
deposit_value = 0
withdraw_value = 0
transfer_value = 0
paybill_value = 0

#Input data
customers.append(input("Your name: "))
customers.append(float(input("Balance: ")))
customers.append(input("Your password: "))
bbl = ATM(customers[0],customers[1],customers[2])

#Check Balance
bbl.check_balance()

#Deposit
dep = input("Do you want to deposit?(y/n): ").lower()
if dep=='y':
    deposit_value = float(input("Deposit Amount: "))
    bbl.deposit(deposit_value)
else:pass

#Withdraw
withdr = input("Do you want to withdraw?(y/n): ").lower()
if withdr=='y':
    withdraw_value = float(input("Withdraw Amount: "))
    if withdraw_value<=100:
        print("Minimum withdraw is 100 THB., Please Try again")
        withdraw_value = float(input("Withdraw Amount: "))
    if withdraw_value > (customers[1]+deposit_value):
        print("Balance is not enough, please Try again")
        withdraw_value = float(input("Withdraw Amount: "))    
    else:bbl.withdraw(withdraw_value)
else:pass

#Transfer
transf = input("Do you want to transfer?(y/n): ").lower()
if transf=='y':
    transfer_value = float(input("Transfer Amount: "))
    payee_name = (input("Transfer to: "))
    if transfer_value > (customers[1]+deposit_value-withdraw_value):
        print("Balance is not enough, please Try again")
        transfer_value = float(input("Transfer Amount: "))
    else:bbl.transfer(transfer_value,payee_name)
else:pass

#Paybill
paybill = input("Do you want to paybill?(y/n): ").lower()
if paybill=='y':
    paybill_value = float(input("Paybill Amount: "))
    payee_bill_name = (input("Payee: "))
    fee_value = float(input("Fee Amount: "))
    if paybill_value > (customers[1]+deposit_value-withdraw_value-transfer_value):print("Balance is not enough, please Try again later.")
    else:bbl.paybill(paybill_value,payee_bill_name,fee_value)
else:pass

#New Name
changename = input("Do you want to change your name?(y/n): ").lower()
if changename=='y':bbl.change_name(input("Do you want to change your name as: "))
else:pass

#New password
changepw = input("Do you want to change your password?(y/n): ").lower()
if changepw=='y':
    len_pw = 6
    while len_pw == 6:
        new_pw=input("Please enter 6 digits[0-9]: ")
        if len(new_pw)==len_pw:
            bbl.change_password(new_pw)
            break
        else:
            print("Invalid password!")



