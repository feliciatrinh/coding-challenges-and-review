"""
Source: Leetcode
Input: non-negative number n
Output: number of prime numbers less than n

Example
Input: 10
Output: 4

Naive
- for every number i less than n, determine if i is prime
- determining if i is prime requires checking if i is divisible by any number less than i
- Runtime: O(n^2), Space: O(1)

Sieve of Eratosthenes
Runtime: O(n log(logn))
Space: O(n)

- we start with number 2
- all multiples of 2 are marked false
- all multiples of 3 are marked false
- skip 4
- for current number p, multiples of p starting at p^2 are marked false
  p^2, p^2 + p, p^2 + 2p, p^2 + 3p, etc. are marked false
"""


def count_primes_naive(n):
    count = 0
    for i in range(2, n):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            continue
        else:
            count += 1
    return count


def count_primes(n):
    prime = [True] * n
    i = 2
    while i * i < n:
        if prime[i]:
            for j in range(i * i, n, i):
                prime[j] = False
        i += 1

    count = 0
    for k in range(2, n):
        if prime[k]:
            count += 1
    return count


assert count_primes_naive(10) == 4
assert count_primes(10) == 4
