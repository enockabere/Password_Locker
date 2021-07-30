 
import unittest # Importing the unittest module
from credential import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for Credentials class behaviours
    
    Args:
        unittest.TestCase: TestCase class that  helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_credentials = Credentials("Instagram","assassin","wtf")
    def test_initialization(self):
        '''
        Test initialization test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.app_name,"Instagram")
        self.assertEqual(self.new_credentials.account_username,"assassin")
        self.assertEqual(self.new_credentials.account_password,"wtf")
    def test_save_credential(self):
        '''
        test case to check whether objects are saved to credential list
        '''
        self.new_credentials.save_logins()
        self.assertEqual(len(Credentials.credentials_list),1)
if __name__ ==  '__main__':
    unittest.main()