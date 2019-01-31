# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:56:33 2018
@author: milly
"""

def Password(truePasscode, balance):
    count = 3
    while True:
        try:
            while count > 0:
                attempt= int(input("Enter Password: "))
                if attempt != truePasscode:
                    count = count -1
                elif attempt == truePasscode:
                    Data_bundle_purchase(truePasscode, balance)
            break
        except ValueError:
            print("Enter a number!")
        print("You have used up all of your attempts!")

def Data_bundle_purchase(truePasscode, balance):
    print(" Would you like to: \n\n Request credit balance (1) \n Purchase data bundle (2) \n Exit the program (3) \n\n>>> ")  
    user_input = 0
    while True:
        try:
            while user_input < 1 or user_input > 3:
                user_input = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Please enter a number!")
    
    if user_input == 1:
        print ("\nYour balance is £{}".format(balance))
        print("Do you want another service? ")
        print("Type yes or no")
        another_service(truePasscode, balance)
        
    elif user_input == 2:
        check_phone_number(truePasscode, balance)
    elif user_input == 3:
        top_up(truePasscode, balance)

def another_service(truePasscode, balance):
    more = ""
    while True:
        try:
            while more != "yes" or more != "no":
                more = input("Please enter your choice: ")
                if more == "yes":
                    Data_bundle_purchase(truePasscode, balance)
                elif more == "no":
                    print("Okay, bye.")
                else:
                    print("Please try again.")
                    another_service(truePasscode, balance)
                break
        except ValueError:
            print("Please enter either yes or no")
            
    
def password_try(truePasscode, balance):
    print("Please type yes or no")
    try_again = input().lower()
    if try_again == "yes":
        Data_bundle_purchase(truePasscode, balance)
    else:
        print("Okay, bye!")
    
    
def checkBalance(balance):
   if balance > 0:
       return True
   else:
       return False
   
def check_phone_number(truePasscode, balance):
    phone_number = "1"
    phone_number_2 = "2"
    
    while True:
        try:
            while phone_number != phone_number_2:
                phone_number = int(input("Please enter your phone number: "))
                phone_number_2 = int(input("Please enter your phone number again: "))
                if phone_number != phone_number_2:
                    print("The numbers you have entered do not match")
                    check_phone_number(truePasscode, balance)
                elif phone_number == phone_number_2:
                    data_amount(truePasscode, balance)
            break
        except ValueError:
            print("Please enter a number to continue.")

def multipleOfFive(amount):
    return amount == int(amount / 5.0) * 5

def data_amount(truePasscode, balance):
    maxTopUp = 100.00
    print("𝗠𝗮𝘅 𝘁𝗼𝗽-𝘂𝗽 𝗮𝗺𝗼𝘂𝗻𝘁 𝗶𝘀 £𝟭𝟬𝟬")
    print("|||Top-up amount must be a multiple of 5 pounds|||")
    print("You have £" + str(balance) + " remaining in your balance.")
    print("Please enter your top-up amount: \n>>>")
    amount = 1
    new_balance = round(balance - amount, 2)
    
    while True:
        try:
            while amount > 0:
                amount = int(input())

                if amount > maxTopUp:
                    print("Amount exceeds maximum permitted top-up")
                    print("Request refused")
                    return "top-up-request:refused"
                
                elif amount > balance:
                    print("Amount exceeds available funds")
                    print("Request refused")
                    return ("top-up-request", amount)
                
                elif amount %5!=0:
                    print("Your top-up amount must be a multiple of 5.")
                
                elif amount == int(amount/5)*5:
                    print("Thank you for purchasing. You now have £" + str(new_balance) +" left in your account.")
                    print("Wouldyou like another service? ")
                    print("Type yes or no: ")
                    another_service = input().lower()
                    if another_service == "yes":
                        Data_bundle_purchase(truePasscode, balance)
                    else:
                        print("Okay, bye.")
            break
        except ValueError:
            print("Please enter a numerical amount to continue")
            data_amount(truePasscode, balance)
            
def top_up(truePasscode, balance):
    print("Currently, your balance is £" + str(balance))
    amount = 1
    balance = balance + amount
    
    while True:
        try:
            while amount > 0:
                amount = int(input("Enter amount you would like to top up by: £ "))
                print("Thank you. You have now topped up your amount by £" + str(amount) + "And your balance is now £" + str(balance))
                print("Would you like another service? ")
                print("Please type yes or no")
                if another_service == "yes":
                    Data_bundle_purchase(truePasscode, balance)
                else:
                    print("Okay, bye.")
        except ValueError:
            print("Please enter a numerical value to continue")
            top_up(truePasscode, balance)


Password(1234, 34.55)                       