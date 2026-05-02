
import unittest

from src.calculations import add,sub,mul,div

class TestCalculations(unittest.TestCase):

    def test_add(self):
         res=add(10,5)
         self.assertEqual(res,15,msg='Addition Err')

    def test_sub(self):
        res = sub(10, 5)
        self.assertEqual(res, 15, msg='Substract Err')


    def test_mul(self):
        res = mul(10, 5)
        self.assertEqual(res, 15, msg='Multipication Err')

    def test_div(self):
         res=div(10,5)
         self.assertEqual(res,15,msg='Division Err')




