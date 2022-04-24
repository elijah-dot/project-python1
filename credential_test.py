import unittest
from credential import Credential

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Elijah","twitter","euregfj")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.username,"Elijah")
        self.assertEqual(self.new_credential.serviceprovider,"twitter")
        self.assertEqual(self.new_credential.userpassword,"euregfj")
    # credential save
    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),1)
       
    # multiple credentials
        
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("test","userservice","userp","personalnumber",)
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list))
     
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credentials_list = []
        
        
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credential to check if we can save multiple contact
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("test","userservice","userp","personalnumber",)
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),2)
        
        
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("test","userservice","userp","personalnumber",)
        test_credential.save_credential()
        
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credentials_list),1)
        
      # find credential
        
    def test_find_credential(self):
        '''
        test to check if we can find a credential by service provider and display information
        '''
        self.new_credential.save_credential()
        test_credential = Credential("test","userservice","userp",)
        test_credential.save_credential()
        
        found_credential = Credential.find_credential("userp")
        
        self.assertEqual(found_credential.userpassword,test_credential.userpassword)
        
    # credential exist
        
    def test_credential_exist(self):
        # test to check if we can return a Boolean  if we cannot find the credential.
        self.new_credential.save_credential()
        test_credential = Credential("test","userservice","userp")
        test_credential.save_credential()
        
        credential_exist = Credential.credential_exist("userp")
        self.assertTrue(credential_exist)
        
            # display credential
    def test_display_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credential(),Credential.credentials_list)       
        
    
if __name__ == '__main__':
    unittest.main()

        
               