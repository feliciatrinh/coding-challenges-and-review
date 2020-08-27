"""
Source: Leetcode
Input: two arrays gas and cost
Output: the starting gas station's index if you can travel around the circular circuit in the clockwise direction,
        otherwise -1

costs cost[i] of gas to travel from station i to its next station i + 1
You begin the journey with an empty tank of gas at one of the stations

- if solution exists, it is unique
- both input arrays non-empty and are the same length
- each element in input arrays is non-neg integer

Example
Input: gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
Output: 3

Input: gas = [2, 3, 4], cost = [3, 4, 3]
Output: -1

Ideas
- For the first example, we do these calculations
gas[0] - cost[0] + gas[1] = 3
3 - cost[1] + gas[2] = 5
5 - cost[2] + gas[3] = 5
5 - cost[3] = 3 >= 0 so we can make the round trip starting from index 0

If we put this all together, it's just checking this at the end
gas[0] - cost[0] + gas[1] - cost[1] + gas[2] - cost[2] + gas[3] - cost[3] >= 0

Let m be an array containing the amount of gas you have left over after leaving stop i.
m[0] = gas[0] - cost[0] and we need gas[0] - cost[0] >= 0 to be true
m[1] = m[0] + gas[1] - cost[1]
m[2] = m[1] + gas[2] - cost[2]

at each i, if m[i] - cost[i] < 0 then you can't go onto the next step. We can then just increment the start point
and keep checking each i

we only use m[i - 1] at each i, so we can replace the m array with something like a remainder variable
Then, it'd be remainder = gas[0] - cost[0]

We always start from 0, so if 0 doesn't work as a starting point, then 1, 2, or some index greater than 0 has to work
- if 1 doesn't end up working then 2 or some higher index has to work and so on
- which is why it works to set start = i + 1 when you get that remainder < 0
"""


def gas_station(gas, cost):
    start = 0
    remainder = 0
    final = 0
    for i in range(len(gas)):
        remainder += gas[i] - cost[i]
        if remainder < 0:
            final += remainder
            remainder = 0
            start = i + 1

    if remainder + final < 0:
        return -1
    return start


assert gas_station([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
assert gas_station([2, 3, 4], [3, 4, 3]) == -1
