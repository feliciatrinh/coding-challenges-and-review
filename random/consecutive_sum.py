"""
Input: positive integer, num
Output: The number of ways to represent num as a sum of 2 or more consecutive positive numbers

Given a long int, find the number of ways to represent it as a sum of 2 or more consecutive positive integers.

Solution: Use the arithmetic sum formula to determine which integers you can start at.
Runtime: linear?

Example: 
Input: 15
1, 2, 3, 4, 5
4, 5, 6
7, 8

Output: 3 ways
Note: if you don't require 2 or more consecutive positive numbers then the number of ways would be 4 b/c it'd include 15

- summing consecutive integers is start + (start + 1) + (start + 2) + ... + (start + end) = num
- for every possible end, we want to solve for the corresponding start and see if start is a valid starting point

We have start + (start + 1) + (start + 2) + ... + (start + end) = num
There are (end + 1) occurrences of start so we can group all the start's together to get:
(end + 1) * start + 1 + 2 + ... + end = num
Use arithmetic sequence formula to get:
(end + 1) * start + end * (end + 1) / 2 = num
Solve for start to get:
(end + 1) * start = num - end * (end + 1) / 2
start = (num - end * (end + 1) / 2) / (end + 1)
"""


def consecutive_sum(num):
    end = 1
    count = 0
    # we don't need to consider any more integers once this sum equals num because any sum
    # of consecutive integers beyond this starting point will exceed num
    while end * (end + 1) / 2 < num:
        start = (num - end * (end + 1) / 2.0) / (end + 1)
        if start > 0 and start.is_integer():
            count += 1
        end += 1
    return count


assert consecutive_sum(15) == 3
