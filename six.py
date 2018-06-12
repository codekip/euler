import unittest

"""
The sum of the squares of the first ten natural numbers is,12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,(1 + 2 + ... + 10)2 = 552 = 3025
Hence the get_difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the get_difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_of_squares(upper_limit):
    return sum([x ** 2 for x in range(1, upper_limit + 1)])


def square_of_sum(upper_limit):
    total = sum([x for x in range(1, upper_limit + 1)])
    return total * total


def get_difference(number_range):
    return square_of_sum(number_range) - sum_of_squares(number_range)


class Test(unittest.TestCase):
    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares(10), 385)
        self.assertEqual(sum_of_squares(20), 2870)

    def test_square_of_sum(self):
        self.assertEqual(square_of_sum(10), 3025)

    def test_get_difference(self):
        self.assertEqual(get_difference(10), 2640)


def answer():
    print(get_difference(100))


if __name__ == "__main__":
    unittest.main()
