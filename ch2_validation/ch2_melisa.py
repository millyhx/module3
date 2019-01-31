############
##TASK 1
############

#phoneNumLen = 11
#user_input = input("What's your mobile number? ")
#if len(user_input) == phoneNumLen:
#    print("Thank you")
#else:
#    print("Error.")

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

#if choice == 1:
#    print("Ms Wu")
#elif choice == 2:
#    print("5 years old")
#elif choice == 3:
#    print("London")

while True:
    try:
        while choice < 1 or choice >3:
            choice = int(input("What is your choice? "))
            
        break
    except ValueError:
        print("Please type a number!")
        
if choice == 1:
    print("Ms Wu")
elif choice == 2:
    print("5 years old")
elif choice == 3:
    print("London")

#USE BREAK TO EXIT THE INFINITE LOOP
        
###########
#TASK 3
###########
#
##CLASS BASED USER INPUT VALIDATION
#class Spam(object):
#    def __init__(self, description, value):
#        if not description or value <= 0:
#            raise ValueError
#        self.description = description
#        self.value = value
#        
#s = Spam('s', 5) #------ GIVING THE CORRECT RANGE
#s = Spam('', -1) #------ GIVING THE INCORRECT RANGE
#print(s.value)
#
##WRITING IT WITH AN ASSERT STATEMENT
#class Pink(object):
#    def __init__(self, description, value):
#        assert description !=""
#        assert value > 0
#        self.description = description
#        self.value = value
#
##CREATED A CLASS CALLED SPAM THAT HAS AN OBJECT AS THE PARAMETER
##WE DEFINED AND INITIALIZED SELF, DESCRIPTION AND VALUE
##IF THE PARAMETER GIVEN IS NOT DESCRIPTION OR THE VALUE DOES NOT
##EQUAL LESS THAN OR EQUALS TO 0 THEN RAISE A VALUE ERROR.