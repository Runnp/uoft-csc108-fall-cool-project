import unittest
import buggy_functions


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(buggy_functions.reverse([]), [], 'Empty list')

    def test_single(self):
        self.assertEqual(buggy_functions.reverse([1]), [1], 'Single item')

    def test_multiple(self):
        self.assertEqual(buggy_functions.reverse([1, 2, 3, 4]), [4, 3, 2, 1], 'Multiple items')

    def test_unchanged(self):
        original = [1, 2, 3]
        buggy_functions.reverse(original)
        self.assertEqual(original, [1, 2, 3], 'Original list unchanged')


if __name__ == '__main__':
    unittest.main()