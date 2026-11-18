import unittest
import buggy_functions


class TestOdds(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(buggy_functions.odds([]), [], 'Empty list')

    def test_one_element(self):
        self.assertEqual(buggy_functions.odds([7]), [], 'One element at even index')

    def test_even_length(self):
        self.assertEqual(buggy_functions.odds([10, 20, 30, 40]), [20, 40], 'Even-length list')

    def test_odd_length(self):
        self.assertEqual(buggy_functions.odds(['a', 'b', 'c']), ['b'], 'Odd-length list')

    def test_input_unchanged(self):
        original = [10, 20, 30, 40]
        buggy_functions.odds(original)
        self.assertEqual(original, [10, 20, 30, 40], 'Input must not be modified')

    def test_v2_mutates_input(self):
        original = [10, 20, 30, 40]
        buggy_functions.odds_v2(original)
        self.assertEqual(original, [10, 20, 30, 40], 'odds_v2 must not mutate input')


if __name__ == '__main__':
    unittest.main()
