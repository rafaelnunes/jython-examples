'''
Created on May 05, 2012

@author: rafael
'''
import unittest

from java.lang import Math, String

class JavaTest(unittest.TestCase):

    def test_pow(self):
        self.assertEqual(Math.pow(5, 3), 125)
        
    def test_string_equals(self):
        str1 = "jython"
        str2 = String("jython")
        
        self.assertEqual(str1, str2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()