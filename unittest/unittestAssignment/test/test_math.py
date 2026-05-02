import unittest
from src.calc import add,sub,div

#testcase
class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2,3),5)

#teardown
class TestList(unittest.TestCase):
    def setUp(self):
        self.my_list=[1,2,3]

    def tearDown(self):
        print("Test completed")

    def test_list_length(self):
        self.assertEqual(len(self.my_list),3)

#multi assert
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("hello".upper(),"Hello")

    def test_isupper(self):
        self.assertFalse("hello".isupper())

#Exception testing
class TestExceptions(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10,0)

#test suite
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,1),2)

class TestSub(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(sub(5,3),2)

if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAdd))
    suite.addTest(unittest.makeSuite(TestSub))

    runner = unittest.TextTestRunner()
    runner.run(suite)
