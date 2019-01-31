import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calc = Calculator()
        self.assertTrue(calc.add(3,3), 6)

    def test_subtraction(self):
        calc = Calculator()
        self.assertTrue(calc.subtract(2,3), -1)     
    
    def test_divide(self):
        calc = Calculator()
        self.assertTrue(calc.divide(1,1), 1)     
        
    def test_multiply(self):
        calc = Calculator()
        self.asserTrue(calc.multiply(10,9), 60)      
        
if __name__ == "__main__":
    unittest.main()
