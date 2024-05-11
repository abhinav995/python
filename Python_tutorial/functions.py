# def message():
#     print("hai")
# message()

# def type():
#     print("bye")
# type()

# def message(name):
#     print("hai"+name)
# message("athira")
# def digit(number1,number2):
#     print(number1+number2)
# digit(22,23)

# def digit(number):
#     print(number*number)
# digit(4)

# def digit(number1,number2,number3):
#     print(number1*number2*number3)
# digit(1,2,3)

# def digit(number):
#     b=int(input("enter limit"))
#     for i in range(1,b+1):
#         c=number*i
#         print(f'{number}*{i}={c}')
# digit(5)        

# def digit(number): 
#     b=0
#     c=1
#     print(b)
#     print(c)
#     for i in range(2,number):
#         d=b+c
#         print(d)
#         b=c
#         c=d
# z=int(input("enter a limit"))
# digit(z)          

# def palindrome(input_string):
#     return input_string == input_string[::-1]
# a=input("enter a string")
# if palindrome(a):
#     print("yes")
# else:
#     print("no")

# a= [3,5,6,7,9,4]
# sum=0
# # for i in a:
# #     sum=sum+i
# # print(sum)   
# for i in a:
#    if i%2 == 0:
#       sum=sum+i
# print(sum)

    
    

# def factorial(a):
#       z=1
#       if a<0:     
#         print("no factorial")
#       elif a == 0 or a == 1:
#         return 1
#       else:
#         for i in range(2,a+1):
#            z=z*i
#         return z
# h=int(input("enter a number"))
# print(factorial(h))     
         
#by using recursive function
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num*factorial(num-1)
# print(factorial(5))
             

# add= lambda x,y:x+y 
# print(add(1,2))             
             
# #password generator
# import random
# def password_generate(digit):
#     character="sdfxgcfvhertyugh23456789#4%$%^&"
#     password=" " 
#     for i in range(digit):
#         password=password+random.choice(character)
#     return password 
# h=int(input("enter a number"))
# password=password_generate(h)
# print(password)   
       
#stone paper scissors
import random
def user():
    user_choice=input("enter rock,paper,scissors").lower()
    while user_choice not in ["rock","paper","scissors"]:
        print("invalid")
        user_choice=input("enter rock,paper,scissors").lower()    
    return user_choice

def computer():
    return random.choice(["rock","paper","scissors"])

def define_winner(user,computer):
    if user == computer:
       return "tie" 
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "rock" and computer == "scissors"):
       return "user win"
    else:
       return "computer win"

def game():           
    user_choice=user()
    computer_choice=computer()
    print(f"you chose:{user_choice}")
    print(f"computer chose:{computer_choice}")
    result = define_winner(user_choice,computer_choice) 
    print(result)
game()
           

