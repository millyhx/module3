import unittest
import sys
from primes import is_prime, countWords

class PrimesTestCase(unittest.TestCase):
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    def test_sys_input(self):
        self.assertIsInstance(sys.argv[0], int) #THE 0 POSITION IS THE FILE NAME
        self.assertTrue(is_prime(sys.argv[0]))
        
    def test_ZeroPrime(self):
        self.assertFalse(is_prime(0))
    def test_negative_number(self):
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index))

class test_countWords(unittest.TestCase):
    def test_Word_Count(self):
        self.assertDictEqual(
                {'foo':2, 'bar': 1},countWords('foo bar foo'))



if __name__ == "__main__":
    unittest.main()

#FIRST WE IMPORT THE UNITTESTING MODULE AS WELL AS SYS AND THE FUNCTION WE
#HAVE WRITTEN IN THE PRIMES.PY FILE.
#A CLASS IS CREATED CALLED PRIMESTESTCASE WHICH TAKES AN INPUT OF TEST CASE METHOD
#A FUNCTION IS CREATED THAT HAS SELF AS THE PARAMETER
#SELF THEN ASSERTS TRUE: WHICH MEANS IS_PRIME WHICH IS THE FUNCTION NAME
#SHOULD EQUAL TRUE WHEN 5 IS ENTERED INTO SELF. 