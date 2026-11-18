import unittest
import buggy_functions


class TestRightStrip(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(buggy_functions.right_strip('', 'x'), '', 'Empty input')

    def test_example(self):
        self.assertEqual(buggy_functions.right_strip('fffabcdefffgfff', 'f'), 'fffabcdefffg', 'Given example')

    def test_no_trailing_match(self):
        self.assertEqual(buggy_functions.right_strip('abc', 'x'), 'abc', 'No matching suffix')

    def test_all_match(self):
        self.assertEqual(buggy_functions.right_strip('xxxx', 'x'), '', 'Every character matches')

    def test_only_trailing(self):
        self.assertEqual(buggy_functions.right_strip('xaxxx', 'x'), 'xa', 'Keep internal characters')


if __name__ == '__main__':
    unittest.main()