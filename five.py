import unittest
from itertools import product

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
divisors = [11, 13, 14, 16, 17, 18, 19, 20]


def is_divisible_by_all(num, upper_limit):
    #divisors = list(range(2, upper_limit + 1))
    combined = list(product(([num] * len(divisors)), divisors))
    if all(x % y == 0 for x, y in combined[:upper_limit]):
        return True
    else:
        return False


def smallest_number(max_number, upper_limit):
    for num in range(1, max_number + 1):
        if is_divisible_by_all(num, upper_limit):
            break
    return num


class TestDivisor(unittest.TestCase):
    def test_divisors(self):
        self.assertTrue(is_divisible_by_all(2520, 10))
        self.assertFalse(is_divisible_by_all(2530, 10))

    def test_number(self):
        self.assertEqual(smallest_number(2530, 10), 2520)

    def test_find_solution(self):
        self.assertEqual(find_solution(10), 2520)



def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in divisors):
            return num
    return None


def answer():
    print(find_solution(20))


if __name__ == "__main__":
    unittest.main()
    # answer()
