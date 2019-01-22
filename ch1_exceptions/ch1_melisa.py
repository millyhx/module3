try:
    f = open('testfile')
except Exception:
    print('Error!')

#THE CONSOLE WILL TRY TO OPEN A TEST FILE
#THE FILE IS NOT FOUND BECAUSE EITHER THE NAME IS WRONG 
#OR THERE IS NO FILE EXTENSION FOR PYTHON TO FIND.
#THEREFORE, THE CONSOLE WILL PRINT ERROR.
    
try:
    f = open('tesfile.txt')
    s1 = not_exists
except Exception:
    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
    

try:
    f = open('tesfile.txt')
    s1 = not_exists
except FileNotFoundError:
    print('Sorry, this file does not exist, or the file name is wrong. Please double check.') 
    
###########
#TASK 1
###########
    
try:
    f= open('testfile.txt')
    s1 = not_exists
except Exception as e:
    print(e)

###########
#TASK 2
########### 
 
try:
     f = open('testfile.txt')
except Exception as e:
     print(e)
else:
    print(f.read())
    f.close()

###########
#TASK 3
###########   

try:f = open('testfile')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally..')
    


try:
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally..')
    
