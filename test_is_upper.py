import unittest
import buggy_functions

class Test_is_uppercase(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(buggy_functions.is_uppercase(""), 
            "Empty string")
    
    def test_all_upper(self):
        self.assertTrue(buggy_functions.is_uppercase("ABCDEF"),
            "Uppercase string")
    
    def test_nonletter(self):
        self.assertFalse(buggy_functions.is_uppercase("A123.,!A"),
            "Non-alphabetic string")
    
    def test_all_lowercase(self):
        self.assertFalse(buggy_functions.is_uppercase("abcdef"),
            "Lowercase string")

    def test_mixed(self):
        self.assertFalse(buggy_functions.is_uppercase("AbCDEF"),
            "Mixed-case string")


unittest.main(exit=False)
