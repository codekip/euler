import unittest
from math import factorial


def factorial_sum(num):
    a = factorial(num)
    ans = list(map(int, str(a)))
    return sum([int(x) for x in ans])


class Test(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial_sum(10), 27)
        self.assertEqual(factorial_sum(100), 648)


if __name__ == "__main__":
    unittest.main()
