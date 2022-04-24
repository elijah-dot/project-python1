from user import User
import run
from random import randint
from password import generate_password

def register():
    print("REGISTER")
    print("-"*30)
    username = input("enter username:  ")
    userpassword = input("enter register password:  ")
    compassword=input("confirm password:   ")
    
    #  validation
    if userpassword == compassword:
        user = User(username,userpassword)
        user.save_user
        print(f"Welcome {username}!you are now registered")
        print("Lets Login")
    else:
       repeat= input("Something has gone wrong. Try again. y/n")
       if repeat == "y":
           print(register())
       else:
           print(exit())
           
def Login():
     print("LOGIN")
     print("-"*30)
     username = input("Enter username: ")
     userpassword = input("enter login password:  ")
     
     user = User(username,userpassword)
     if user is None:
         print("please enter a valid name and password")
     else:
         user.login
         print(f"Welcome {username}!you are logged in")
         print("\n")
         print("-"*30)
         print('What would you like to do?')
         while True:
            print("use this short codes : cc-create a new password , dc-display passwords for different userservice,fc-find a specific password,dd-delete,ex -exit" )
            print("-"*50)
            useranswer = input("answer: ")
            if useranswer == "cc":
               