import json
import sys
import random 
import os
from datetime import datetime

customer_file="customers.txt"
staff_file = "staffs.txt"
customer_data=[]
user_session = "user_session.txt"



#staff data 
data = {}
data["staff"] = []
data["staff"].append({
    "fullname": "Charles Barber",
    "username": "charlieb",
    "password": "cha7l13",
    "email": "charlieb@email.com"
})
data["staff"].append({
    "fullname": "Larry Google",
    "username": "larryg",
    "password": "largo",
    "email": "largo@email.com"
})
#A function to write data to a file 
def write_data(file_name, file_contents):
    with open(file_name, "w") as staff_file:
        json.dump(file_contents, staff_file)


#checks the user login from file before granting access
def check_login():    
    with open('staffs.txt') as json_file:
        data = json.load(json_file)
        global username
        username = input("Username: ")
        password =input("Password: ")
        for p in data['staff']:
            if p["username"] == username and p["password"] == password:
                x = p["username"] 
                y = p["password"]
                x == y  is True
                #logs the sign in time and date and saves it to a txt file 
                login_time= username +" "+ "signed-in at " + str(datetime.now())
                write_data(user_session, login_time) 
                print (f"You are logged in as {username}")
                user_menu()
                
                break
        else:
            print("Invalid details...Try again!!!")
            check_login()

#Main menu for before login 
def main_menu():
    print("1. Staff Login ")
    print("2. Close app")
    menu_option = input("Select an option: ")
    
    if menu_option == "2":
        sys.exit()
        
    elif menu_option == "1":
        print("Enter login details: ")
        check_login()
        
    else:
        print("Enter a valid input!!!")
        main_menu()
    # except:
        #     ("Enter a number 1 or 2")
        #     main_menu()
#After the user logs in he can use any of the features below 
def user_menu():
    print ("1. Create new bank account ")
    print ("2. Check account details")
    print ("3. Logout")
    menu_selection=input()
    if menu_selection == "1":
        print ("Enter the customer's information ")
        account_name = input("Account name: ")
        opening_balance = input("Opening Balance: ")
        account_type= input("Account Type: ")
        email= input("Customer's email: ")
        #Generate a random account Number 
        account_number = random.randint (1000000000, 9999999999)
        #append customer data to a list 
        customer_data.append([account_name,opening_balance,account_type,email, account_number])
        print(customer_data)
        #write customer data to file
        write_data(customer_file, customer_data)
        print("Account successfully created!!!")
        print (f"Your account number is {account_number}")
        user_menu()
#feature tp check the account number from  file 
    elif menu_selection == "2":
        check_account = int(input("Enter your account number: "))
        print (f"Your account number is {check_account}")
        with open(customer_file) as json_file:
            data = json.load(json_file)
            if int(data[0][4]) == check_account:
                print (f"Your Account balance is {data[0][1]}")
                user_menu()
            else:
                print("Account not found")
                user_menu()
#Log out and return to the main menu 
    elif menu_selection == "3":
        logout_time= username +" "+ "signed-out at " + str(datetime.now())
        write_data(user_session, logout_time)
        print(logout_time) 
        os.remove("user_session.txt")
        main_menu()
    else:
        ("Invalid input!!!")
        user_menu()

write_data(staff_file, data)
main_menu()
check_login()



    