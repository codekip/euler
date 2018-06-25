import unittest
from math import pow
from functools import reduce


def power(n):
    ans = int(pow(2, n))
    strv = list(str(ans))
    return reduce(lambda x, y: int(x) + int(y), strv)


class Test(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(5), 5)
        self.assertEqual(power(15), 26)

    def test_answer(self):
        self.assertEqual(power(1000), 1366)


if __name__ == "__main__":
    unittest.main()
