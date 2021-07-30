class User:
    """
    Class that generates new instances of users.
    """

    myUser = [] # Empty contact list

    def __init__(self,username,password):

      # Create instances of objects

        self.username = username
        self.password = password
    def save_user(self):
        
        '''
        method saves user objects to the user list
        '''
        User.myUser.append(self)
    def delete_user(self):
        '''
        method to delete a user object
        '''
        User.myUser.remove(self)
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and return a string that matches that username

        Args:
            username: username to search for
        Returns :
            matching username
        '''
        for user in cls.myUser:
            if user.username == username:
                return user