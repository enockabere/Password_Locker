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
    