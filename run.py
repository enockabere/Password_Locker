#!/usr/bin/env python3.6
from user import User
from credential import Credentials

def create_user(username,password):
    '''
    Function to create new user
    '''
    myUser = User(username,password)
    return myUser

            
