#PRIME NUMBER TASK

def is_prime(number):
    if number <= 1:
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True

#CREATE A FUNCTION CALLED IS_PRIME WITH THE PARAMETER NUMBER
#IF NUMBER IS LESS THAN OR EQUAL TO 1
#RETURN FALSE
#FOR EACH ELEMENT IN THE RANGE OF 2 TO THE NUMBER VALUE
#MODULUS (%) FINDS THE REMAINDER AFTER DIVISION OF BOTH NUMBERS.
#IF THE MODULUS OF NUMBER BY ELEMENT IS EQUAL TO 0 THEN
#RETURN FALSE
#OTHERWISE RETURN TRUE.
    
def prime_next_number(number):
    index = number
    while True:
        index += 1
        if is_Prime(index):
            print(index)

#COUNTWORD TASK

def countWords(text):
    dict = {}
    
    for word in text.split():
        print(word)
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict


        