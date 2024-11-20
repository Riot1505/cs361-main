from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import config
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import base64

from currency_converter import CurrencyConverter

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
    def getUsername(self):
        return self.username

SignedinUser = User("1", "1", "1", "1")

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def login():
    global SignedinUser
    username = input("Add username: ")
    password = input("Add password: ")
    
    connect = get_db_connection()
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user_data = cursor.fetchone()
    connect.close()

    if user_data and check_password_hash(user_data['password'], password):
        SignedinUser = User(user_data['id'], user_data['username'], user_data['email'], user_data['password'])
        print("Successful Login! The user does exist in the database.")
    else:
        print("Invalid username or password")

def logout():
    global SignedinUser
    if SignedinUser.getUsername() != "1":
        SignedinUser = User("1", "1", "1", "1")
        print("Successfully logged out.")
    else:
        print("You were already logged out.")

def register():
    global SignedinUser

    if(SignedinUser.username != '1'):
        print("You are currently logged in. Registration is only possible when you are logged out.")
        return

    username = input("Add your username: ")
    email = input("Add your email: ")
    password = input("Add your password (Ensure it is at least 10 elements long): ")

    if(len(password) < 10):
        print("The password is not long enough...")
        return

    hashed_password = generate_password_hash(password)

    connect = get_db_connection()
    cursor = connect.cursor()
    try:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                           (username, email, hashed_password))
            connect.commit()
            print("You have successfully added your account!")
    except:
        print("Username or email already exists.")
    finally:
        connect.close()

def changepass():
    global SignedinUser
    if(SignedinUser.username == '1'):
        print("You are currently not logged in, so password change is not possible.")
        return
    
    username = SignedinUser.username
    newpass = input("Please input your new password (10 elements long minimum): ")
    confpass = input("Please confirm your new password: ")
    oldpass = input("Please input your old password: ")

    if(len(newpass) < 10):
        print("The new password is too short.")
        return

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user_data = cursor.fetchone()
    if newpass == confpass:
        if user_data and check_password_hash(user_data['password'], oldpass):
            try:
                hashed_password = generate_password_hash(newpass)
                cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password, username))
                conn.commit()
                print('Changing password successful!', 'success')
            except:
                print('Invalid username or password.', 'error')
            finally:
                conn.close()
        else:
            print("The old password is incorrect.")
    else:
        print("The new password doesn't match the confirmation password.")


def foreigncurr():
    foreigncurrency = input("Please input the foreign currency you want to convert to: ")
    foreignc = CurrencyConverter()
    connect = get_db_connection()
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM items')

    alldata = cursor.fetchall()
    try:
        for data in alldata:
            foreignvalue = str(foreignc.convert(float(data['price']), data['currency'], foreigncurrency))
            cursor.execute("UPDATE items SET price = ?, currency = ? WHERE id = ?", (str(round(float(foreignvalue), 2)), foreigncurrency, data['id']))
            connect.commit()
            print("The item ID: ", data['id'], "The item price: ", data['price'], "The items currency: ", data['currency'])
    except:
        print("Invalid currency.")
    finally:
        connect.close()

def choices(userval):
    match userval:
        case "1":
            login()
            return True
        case "2":
            logout()
            return True
        case "3":
            register()
            return True
        case "4":
            changepass()
            return True
        case "5":
            foreigncurr()
            return True
        case "6":
            return False
        case _:
            print("Invalid input. Please enter again.")
            return True

process1 = True

Options = "Choose an option via the associated numeric value:\n\
          1. Login\n\
          2. Logout\n\
          3. Register\n\
          4. change password\n\
          5. foreign currency conversion\n\
          6. Exit"

print(Options)
while(process1):
    userval = input("Add input: ")
    process1 = choices(userval)
