import unittest
import buggy_functions


class TestIsUppercase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(buggy_functions.is_uppercase(''), True, 'Empty string')

    def test_all_upper(self):
        self.assertEqual(buggy_functions.is_uppercase('ABCDEF'), True, 'All uppercase')

    def test_nonletter(self):
        self.assertEqual(buggy_functions.is_uppercase('A123.,!A'), False, 'Nonletter')

    def test_all_lowercase(self):
        self.assertEqual(buggy_functions.is_uppercase('abcdef'), False, 'All lowercase')

    def test_mixed(self):
        self.assertEqual(buggy_functions.is_uppercase('AbCDEF'), False, 'Mixed case')


if __name__ == '__main__':
    unittest.main()