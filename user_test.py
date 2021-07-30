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
        self.newUser = User("Enock","Enock123") # create contact object
    def tearDown(self):
        '''
        tearDown does cleanup after every test case has run
        '''
        User.myUser = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.newUser.username,"Enock")
        self.assertEqual(self.newUser.password,"Enock123")
        
    def test_save_user(self):
        '''
        test_save_user test case to test if user object is saved into the user list
        '''
        self.newUser.save_user() # saving a new user
        self.assertEqual(len(User.myUser),1)
        
    def test_save_multi_users(self):
        '''
        test_save_multi_user test case to test if we can save multiple objects to our contact lists
        '''
        self.newUser.save_user()
        test_user = User("Aiden","Aiden1234") #new user
        test_user.save_user()
        self.assertEqual(len(User.myUser),2)
    def test_delete_user(self):
        '''
        test_delete_user test case to test if we can delete a user object from our user list
        '''
        self.newUser.save_user()
        test_user = User("Aiden","Aiden1234")
        test_user.save_user()
        
        self.newUser.delete_user() #deleting a user
        self.assertEqual(len(User.myUser),1)
    def test_find_user_by_username(self):
        '''
        test to check if we can retrieve a user by username and display information
        '''
        self.newUser.save_user()
        test_user = User("Aiden","Aiden1234")
        test_user.save_user()
        
        found_user = User.find_by_username("Aiden")
        self.assertEqual(found_user.password,test_user.password)
    

if __name__ ==  '__main__':
    unittest.main()
