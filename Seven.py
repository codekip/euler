import unittest
import math

""" LEARNT: Sieve of eratosthenes algorithm to solve this
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
sieve from - https://codereview.stackexchange.com/a/102532/101643
"""


def primes_using_sieve_of_erastothenes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    sq_root = int(math.sqrt(limit)) + 1

    for i in range(2, sq_root):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

    return [i for i, number in enumerate(sieve) if number]


def prime_at(position, max):
    return primes_using_sieve_of_erastothenes(max)[position - 1]


class Test(unittest.TestCase):
    def test_primes(self):
        self.assertEqual(primes_using_sieve_of_erastothenes(10), [2, 3, 5, 7])
        self.assertEqual(
            primes_using_sieve_of_erastothenes(20), [2, 3, 5, 7, 11, 13, 17, 19]
        )


    def test_return_prime_at_position(self):
        self.assertEqual(prime_at(2, 10), 3)
        self.assertEqual(prime_at(10001, 200000), 104743)


if __name__ == "__main__":
    unittest.main()
