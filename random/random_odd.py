"""
Input: interval a, b
Output: a random odd integer in the range of a to b with equal probability

Range is inclusive.

Given a random function random(a, b) that returns a random integer in the range of a to b, implement a randomOdd(a, b)
function that returns a random odd integer in the range of a to b

random.randrange(start,  stop [,  step]) returns a randomly selected integer from range(start, stop, step)
Example: random.randrange(2, 20, 2) would return a random integer between 2 and 20 such as 2, 4, 6, 8...18.

But we need to use the provided random() function instead.

Notes
- you can get always get an odd number by calculating 2 * (num // 2) + 1
- cases possible: a is odd, b is odd
                  a is odd, b is even
                  a is even, b is odd
                  a is even, b is even
  Example
  (1, 5) gives 1, 2, 3, 4, 5
  (1, 4) gives 1, 2, 3, 4
  (2, 5) gives    2, 3, 4, 5
  (2, 6) gives    2, 3, 4, 5, 6

- just using the rule 2 * (num // 2) + 1 gives you the following distribution, which isn't what you want

  1, 3, 3, 5, 5
  1, 3, 5
  3, 3, 5, 5
  3, 3, 5, 5, 7

  - In case 1, you'd need to subtract 1 from a and then call the function again
  - In case 2, subtract 1 from a and b
  - In case 3, do nothing
  - In case 4, subtract 1 from b
"""
from random import randint
from collections import Counter


def random(a, b):
    return randint(a, b)


def odd_random(a, b):
    if a % 2 != 0:
        if b % 2 != 0:
            return odd_random(a - 1, b)
        return odd_random(a - 1, b - 1)
    if b % 2 == 0:
        return odd_random(a, b - 1)
    return 2 * (random(a, b) // 2) + 1


# Testing
intervals = [(1, 5), (2, 5), (1, 4), (2, 6)]
result = []
for interval in intervals:
    a, b = interval
    nums = Counter()
    for _ in range(1000):
        num = odd_random(a, b)
        nums[num] += 1

    total = sum(nums.values())
    for k, v in nums.items():
        nums[k] = v / total
    result.append(nums)

print(result)
