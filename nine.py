import unittest
from itertools import combinations

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.
"""


def is_pythagorean_triangle(lst):
    lst = sorted(lst)

    if len(lst) != 3:
        return False

    return (lst[0] * lst[0]) + (lst[1] * lst[1]) == (lst[2] * lst[2])


# AP function - Learnt use of combination !
def combine(product):
    for x, y in combinations(range(1, product - 1), 2):
        z = product - x - y
        if z > 0:
            if is_pythagorean_triangle([x, y, z]):
                return x * y * z


class Test(unittest.TestCase):
    def test_known_input(self):
        self.assertTrue(is_pythagorean_triangle([4, 3, 5]))
        self.assertFalse(is_pythagorean_triangle([5, 6, 7]))
        self.assertFalse(is_pythagorean_triangle([5]))

    def test_combine(self):
        self.assertEqual(combine(1000), 31875000)


if __name__ == "__main__":
    unittest.main()
