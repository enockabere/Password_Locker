#!/usr/bin/env python3.6
from user import User
from credential import Credentials

def create_user(username,password):
    '''
    Function to create new user
    '''
    myUser = User(username,password)
    return myUser
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
def delete_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()
