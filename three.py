import unittest


def modified_primes_using_sieve_of_erastothenes(limit):
    sieve = [True] * (int(limit ** 0.5) + 1)
    sieve[0] = sieve[1] = False
    sq_root = int(limit ** 0.5) + 1

    for i in range(2, sq_root):
        if sieve[i]:
            if i < sq_root:
                for j in range(i * i, sq_root, i):
                    sieve[j] = False
            yield i


def max_prime(num):
    primes = modified_primes_using_sieve_of_erastothenes(num)
    ans = 0
    for value in primes:
        if num % value == 0:
            ans = value
    return ans


class Test(unittest.TestCase):
    def test_max_prime(self):
        self.assertEqual(max_prime(10), 2)
        self.assertEqual(max_prime(100), 5)
        self.assertEqual(max_prime(1000), 5)

    def test_answer(self):
        self.assertEqual(max_prime(600_851_475_143), 6857)


if __name__ == "__main__":
    unittest.main()
