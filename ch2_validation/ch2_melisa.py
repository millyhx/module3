###########
#TASK 1
###########

phoneNumLen = 11
user_input = input("What's your mobile number? ")
if len(user_input) == phoneNumLen:
    print("Thank you")
else:
    print("Error.")

#HERE I HAVE SET THE LENGTH OF A PHONE NUMBER
#THEN I ASKED THE USER FOR THEIR PHONE NUMBER
#IN THE IF FUNCTION I'VE STATED THAT IF THE PHONE NUMBER
#IS THE SAME LENGTH AS WHAT IT SHOULD BE THEN PRINT THANK YOU
#IF IT IS NOT THEN PRINT ERROR.
    
###########
#TASK 2
###########
    
print("***choice***")
print("1.Display my name")
print("2.Display my age")
print("3.Display my city")

choice = 0
choice = int(input("What is your choice? "))

if choice == 1:
    print("Ms Wu")
elif choice == 2:
    print("5 years old")
elif choice == 3:
    print("London")

while True:
    try:
        while choice < 1 or choice > 3:
            choice = int(input("What is your choice? "))
            break
    except ValueError:
        print("please type a number")




