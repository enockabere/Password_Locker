import unittest #Here we are importing the unitest module
from user import User #Import the user class for testing

class testUser(unittest.TestCase):
    '''
    testUser subclass defines the test cases for the User class behaviors
    
    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.myUser = User("Enock","Enock123") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.myUser.username,"Enock")
        self.assertEqual(self.myUser.password,"Enock123")

if __name__ == '__main__':
    unittest.main()
