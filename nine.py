import unittest

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

def candidate(lst):
    if map(lambda x: x%2 == 0,lst)


class Test(unittest.TestCase):
    def test_known_input(self):
        self.assertTrue(is_pythagorean_triangle([4, 3, 5]))
        self.assertFalse(is_pythagorean_triangle([5, 6, 7]))
        self.assertFalse(is_pythagorean_triangle([5]))

    def test_get_candidates(self):
        self.assertTrue(candidate([3, 4, 5]))


if __name__ == "__main__":
    unittest.main()
