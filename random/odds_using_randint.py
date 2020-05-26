"""
Input: Inclusive interval a, b
Output: all odd numbers in [a, b] using randint with equal probability

random.randint return an integer N where a <= N <= b
"""
from random import randint


def odds_using_randint(a, b):
    length = b - a + 1
    num_odds = length // 2
    if a % 2 != 0 and b % 2 != 0:
        num_odds += 1

    odds = set()
    while len(odds) < num_odds:
        num = randint(a, b)
        if num % 2 != 0:
            odds.add(num)
    return odds


assert odds_using_randint(1, 5) == {1, 3, 5}
assert odds_using_randint(2, 2) == set()
assert odds_using_randint(1, 1) == {1}
assert odds_using_randint(2, 4) == {3}
assert odds_using_randint(1, 6) == {1, 3, 5}
