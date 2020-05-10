"""
Input: an array of non-neg integers that rep the height of a bar in a histogram
Output: units of water you can trap in the histogram

Example 1
Input: [5, 3, 2, 5]
Output: 5
- 2 units above bar of height 3 and 3 units above bar of height 2

Example 2
Input: [1, 0, 2]
Output: 1

Example 3
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Subproblem: T(i), amount of water that can be stored up to index i

Recurrence relation:
T(i) = min {max_left[i], max_right[i]} - height[i] + T(i-1)
final answer is T(len - 1)

- max_left is array storing the maximum height of bar from
  the left end up to index i
- max_right is array storing the maximum height of bars seen starting from the
  right end to index i

- When updating max_left, the next element is the
  max{last element, height of bar i} iterating from left to right
- When updating max_right, the next element is the
  max{last element, height of bar i} iterating from right to left

Runtime: O(n) because we iterate through the heights twice to create max_left
and max_right then we iterate through n once more to get our answer.

Notes: 
- can use stack or 2 pointers method to only have to iterate through the heights once?
https://leetcode.com/articles/trapping-rain-water/
"""

def trap_rain_water(height):
    if len(height) < 3:
        return 0

    max_left = [height[0]]
    max_right = [height[-1]]
    # max height of bars seen from the left end to index i
    for h in height[1:]:
        max_left.append(max(max_left[-1], h))
    # max height of bars seen from the right end to index i
    for h in height[-2::-1]:
        max_right.insert(0, max(max_right[0], h))

    # add up the amt of water stored at each bar
    t_curr = 0
    for i in range(len(height)):
        t_curr += min(max_left[i], max_right[i]) - height[i]
    return t_curr


assert trap_rain_water([5, 3, 2, 5]) == 5
assert trap_rain_water([1, 0, 2]) == 1
assert trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert trap_rain_water([]) == 0
assert trap_rain_water([4]) == 0
assert trap_rain_water([2, 3]) == 0
