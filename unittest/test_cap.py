'''
This test tests whether each word in a string starts with a capital letter.
'''

import unittest 
import cap1, cap2

class test_cap1(unittest.TestCase):

    def test_1(self):
        result= cap1.cap('python')
        self.assertEqual(result, 'Python')

    def test_2(self):
        result=cap1.cap('monty python')
        self.assertEqual(result, 'Monty Python')

class test_cap2(unittest.TestCase):

    def test_1(self):
        result= cap2.cap('python')
        self.assertEqual(result, 'Python')

    def test_2(self):
        result=cap2.cap('monty python')
        self.assertEqual(result, 'Monty Python')

if __name__=='__main__': #runs only when the script is run directly
    unittest.main()