import unittest
from functools import reduce
from itertools import product


"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def calculate(numbers):
    return reduce((lambda x, y: x * y), numbers)


def is_pallindrome(result):
    str_result = str(result)
    rev = str_result[::-1]

    return str_result == rev


def combine_lists(a, b):
    return list(product(a, b))


def multiply(a, b):
    return max([x * y for x, y in combine_lists(a, b) if is_pallindrome(x * y)])


class TestPallindrome(unittest.TestCase):
    def test_pallindrome_result(self):
        self.assertEqual(calculate([91, 99]), 9009)
        self.assertEqual(calculate([11, 11]), 121)

    def test_is_pallindrome(self):
        self.assertTrue(is_pallindrome(909))
        self.assertTrue(is_pallindrome(9009))
        self.assertFalse(is_pallindrome(9139))

    def test_combine_lists(self):
        self.assertEqual(
            combine_lists(range(1, 3), range(3, 5)), [(1, 3), (1, 4), (2, 3), (2, 4)]
        )

    def test_multiply(self):
        self.assertEqual(multiply(range(1, 3), range(3, 5)), 8)
        self.assertEqual(multiply(range(90, 100), range(90, 100)), 9009)
        self.assertEqual(multiply(range(100, 1000), range(100, 1000)), 906609)


def max_pallindrome():
    print(multiply(range(100, 1000), range(100, 1000)))


if __name__ == "__main__":
    unittest.main()
