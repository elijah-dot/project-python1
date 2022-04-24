from ast import Delete

class Credential:
    credentials_list = []
    
    def __init__(self,username,serviceprovider,userpassword):
        
        self.username = username
        self.serviceprovider= serviceprovider
        self.userpassword= userpassword