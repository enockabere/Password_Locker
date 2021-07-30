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
    def tearDown(self):
        '''
        tearDown does cleanup after every test case has run
        '''
        Credentials.credentials_list = []
    def test_init(self):
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
    def test_save_multi_accounts(self):
        '''
        test case to check if we can save multiple accounts
        '''
        self.new_credentials.save_logins()
        test_login = Credentials("Twitter","hello","123") #new login
        test_login.save_logins()
        self.assertEqual(len(Credentials.credentials_list),2)
    def test_delete_login(self):
        '''
        test case to test if we can delete credential object from our list
        '''
        self.new_credentials.save_logins()
        test_login = Credentials("Twitter","hello","123")
        test_login.save_logins()
        
        self.new_credentials.delete_logins()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_find_login_by_appName(self):
        '''
        test to check if we can retrieve username  by app name and display information
        '''
        self.new_credentials.save_logins()
        test_login = Credentials("Twitter","hello","123")
        test_login.save_logins()
        
        found_login = Credentials.find_by_appName("Twitter")
        self.assertEqual(found_login.account_username,test_login.account_username)
if __name__ ==  '__main__':
    unittest.main()