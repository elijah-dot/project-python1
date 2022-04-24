#!/usr/bin/env python3.10
from credential import Credential
import login
 
#create credential

def create_credentials(usname,sprovider,uspassword):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(usname,sprovider,uspassword)
    return new_credential

# save credential
def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()
        
# delete credential
def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_contact()
        
def find_credential(serviceprovider):
    '''
    Function that finds a credential by serviceprovider and returns the credential
    '''
    return Credential.find_credential(serviceprovider)

def check_exixting_credentials(serviceprovider):
    '''
    Function that check if a credential exists with that service provider and return a Boolean
    '''
    return Credential.credential_exist(serviceprovider)

def  display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credential()

# main function

def main():
        print("Hi,welcome to our password generator app,")
        ans=input("would you like to generate a password? y for YES or n for NO:  ")
        if ans == "y":
                status = input("are you a registered user?  y/n?")
                if status == "n":
                        login.register()
                        login.Login()
                else:
                        login.Login()
                        
if __name__ == '__main__':

     main()                        
                      
                       