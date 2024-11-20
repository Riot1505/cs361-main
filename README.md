# Foreign Currency Rate Microservice and change password, login, and register functionalities.
This microservice creates a foreign currency rate, where the price of items on the website will be converted to the appropriate currency of the users desire. For example,
if the user wants to switch from USD price to GBP, then they can do so under this microservice. To use the change password functionality, you will have to specify
input of the new password, confirm that password, and then put in the old password. To login, you have to input your username and password. For the reigster, you have
to add the username, password, and email.

## Test program programmatically make a request
To make a request for data, the user will have to specify the foreign currency that they want to change to. Here is the following command and the explanation:

### Commands
#### Foreign currency
Write the currency rate in its shorthand form (e.g. United States Dollar is USD)
```
USD
```
If you want Great Britains Pound, then do this:
```
GBP
```
I have also added a change password functaionlity to the code, because that was also part of the microservice. Here is the following command and the explanation:

### Commands
#### Change Password
Write the username of the account, write the new password, write the new password again, and then write the old password.
```
new password
confirm password
old password
```
This will create a new password for the logged in user.

The following functionalities to the code seems to be already written by the time I was doing the microservice, this includes the register and login functionality. I did 
have to re-construct it for the test program. Here is the following commands and the explanation:

### Commands
#### Login
Write the username and password.
```
username
password
```
#### Register
Write the username, email, and password.
```
username
email
password
```


## Test program programmatically receive data
To receive data from the microservice, it should be done automatically for you, as it will print out all of the items in the website, and its corresponding price
based on the foreign currency of the users choosing. For the change password functionality, the user will have to log out of their current account and log back in
and use the new password. The new password will then be accepted for the existing account. Register is done automatically by logging into that created account.
The login functionality will receive data by giving data that is contained for that specific account.

### Responses
#### Foreign Currency
The test program should print out all the values in terms of that foreign currency that it received from the program (Note, make sure to do the foreign currency again to see the difference.)
Example response:
```
The item ID: 1 The Item Price: 100 The Items currency: USD
```

#### Change Password
If you were to log out of your account and log back in with the new password, the program should receive data of that new password.
Example response:
```
Successful login! The user does exist in the database.
```
This is the standard output of logging in, but if the new password is sent to the database and received, then it should get to this page from the program
receiving a new password.

#### Login
By logging into the program, the program will naturally receive data, because it needs to check the username and password that the user inputted against the database itself.
Example response:
```
Successful login! The user does exist in the database.
```

#### Register
When registering, it should be added straight into the database. This can then be retrieved by logging into the account through the login feature.
Example response:
```
Successful login! The user does exist in the database.
```

Important note: When I was starting out on the microservice, it seems as though 2 out of the 3 user stories were already almost fleshed out, which were the logins and registers. I added extra
lines of codes to create the test program for it.

# UML Design Sequence
This includes two different UML, one for change password and the other for the foreign currency rate. It shows how requests and receives data is done.
![UML1](https://github.com/user-attachments/assets/35617f6b-7955-4c75-a9e2-32c6f824e6a3)
![UML2](https://github.com/user-attachments/assets/1400f454-f8b8-4fc0-8621-b43a98da9bfb)
