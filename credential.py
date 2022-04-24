from ast import Delete

class Credential:
    credentials_list = []
    
    def __init__(self,username,serviceprovider,userpassword):
        
        self.username = username
        self.serviceprovider= serviceprovider
        self.userpassword= userpassword
        
        
        # savecredential
    def save_credential(self):
        
        '''
        save_contact method saves credential objects into credential_list
        '''                   
                   
        Credential.credentials_list.append(self)
     # Delete credentials
    
    def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''
        Credential.credentials_list.remove(self)
        