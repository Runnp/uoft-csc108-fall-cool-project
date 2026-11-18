import unittest
import buggy_functions


class TestReverseInPlace(unittest.TestCase):
    def test_empty(self):
        values = []
        self.assertEqual(buggy_functions.reverse_in_place(values), None, 'Return None')
        self.assertEqual(values, [], 'Empty list unchanged')

    def test_even(self):
        values = [1, 2, 3, 4]
        buggy_functions.reverse_in_place(values)
        self.assertEqual(values, [4, 3, 2, 1], 'Even number of items')

    def test_odd(self):
        values = [1, 2, 3]
        buggy_functions.reverse_in_place(values)
        self.assertEqual(values, [3, 2, 1], 'Odd number of items')

    def test_single(self):
        values = ['a']
        buggy_functions.reverse_in_place(values)
        self.assertEqual(values, ['a'], 'Single item')


if __name__ == '__main__':
    unittest.main()