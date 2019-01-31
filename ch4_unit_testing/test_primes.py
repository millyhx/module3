import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_four_not_prime(self):
        self.assertTrue(is_prime(4), msg="Four is not prime!")
        
    def test_is_zero_not_prime(self):
        self.assertFalse(is_prime(0))
    
    def test_negative_number(self):
        self.assertFalse(is_prime(index))
        
if __name__ == "__main__":
    unittest.main()

