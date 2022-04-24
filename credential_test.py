import unittest
from credential import Credential

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential("Elijah","twitter","euregfj")
    
    def test_init(self):
        self.assertEqual(self.new_credential.username,"Elijah")
        self.assertEqual(self.new_credential.serviceprovider,"twitter")
        self.assertEqual(self.new_credential.userpassword,"euregfj")
        