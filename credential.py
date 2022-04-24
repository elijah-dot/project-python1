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
        
         # finding a credential
    @classmethod 
    
    def find_credential(cls,serviceprovider):
        '''
        Method that takes in a service provider and returns a credential that matches that service provider.
        Args:
            serviceprovider: service provider to search for
        Returns :
            Credential of person that matches the service provider.
        '''
        
        for credential in cls.credentials_list:
            if credential.serviceprovider == serviceprovider:
                return credential
            
            # check if it exist
    @classmethod
    def credential_exist(cls,serviceprovider):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            serviceprovider: serviceprovider to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credentials_list:
            if credential.serviceprovider == serviceprovider:
                return True
        return False
            
        