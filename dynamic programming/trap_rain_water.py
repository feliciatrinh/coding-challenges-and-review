"""
Input: an array of non-neg integers that rep the height of a bar in a histogram
Output: units of water you can trap in the histogram

Example
Input: [5, 3, 2, 5]
Output: 5 units
- 2 units above bar of height 3 and 3 units above bar of height 2

Input: [1, 0, 2]
Output: 1 unit of water

Subproblem: T(i), amount of water that can be stored up to index i

Recurrence relation:
T(i) = min {max_left[i], max_right[i]} - height[i] + T(i-1)
final answer is T(len - 1)

- max_left is array storing the maximum height of bar from
  the left end up to index i
- max_right is array storing the maximum height of bar starting from the
  right end

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
    max_left = [height[0]]
    max_right = [height[-1]]
    for h in height[1:]:
        max_left.append(max(max_left[-1], h))
    for h in height[-2::-1]:
        max_right.append(max(max_right[-1], h))

    t_prev = 0
    for i in range(len(height)):
        t_curr = min(max_left[i], max_right[i]) - height[i] + t_prev
        t_prev = t_curr
    return t_curr

assert trap_rain_water([5, 3, 2, 5]) == 5
assert trap_rain_water([1, 0, 2]) == 1
