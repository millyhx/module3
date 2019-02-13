###########################
#PHONEBOOK TESTING
###########################

import unittest
import sys


#CHECK THE DATABASE EXISTS
def check_db():
    if exists(db_path):
        return True
    else:
        return False
    
class db_Test(unittest.TestCase):
    def test_db(self):
        self.assertTrue(check_db(sys.args[1]))
        
if __name__ == "__main__":
    unittest.main()
    



#THE CHECK DB FUNCTION IS TAKEN FROMTHE MAIN PROJECT
#WHERE IT CHECKS THAT THE DATABASE EXISTS.
#IF THE PATH TO THE DATABSE EXISTS THEN RETURN TRUE
#OTHERWISE RETURN FALSE
#THE CLASS CALLED DB TEST IS TESTING TO CHECK THAT 
#THE ABOVE FUNCTION IS ALSO CORRECT. 
    