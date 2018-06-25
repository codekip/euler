import unittest
import functools

"""Sum of even fibonacci numbers whose values < 4 million.
LEART - functools lrucache ! """


@functools.lru_cache(None)
def fib(n):
    """ 0,2 instead of 0,1  and a + 4 * b instead of b, a + b produces only even numbers"""

    a, b = 0, 2
    c = 1

    x = list()
    while c < n:
        a, b = b, a + 4 * b
        c += 1
        x.append(a)
    return x


class Test(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(sum(fib(12)), 4613732)


if __name__ == "__main__":
    unittest.main()
