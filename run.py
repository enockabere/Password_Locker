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
def find_by_number(username):
    '''
    Function to find user by the username
    '''
    return User.find_by_username(username)
def user_exists(username,password):
    '''
    Function to authenticate user
    '''
    return User.user_exists(username,password)
def display_user():
    '''
    Function to show all saved users
    '''
    return User.display_users()
def create_credentials(app_name,account_username,account_password):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(app_name,account_username,account_password)
    return new_credentials
