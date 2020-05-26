"""
Source: leetcode
Input: n non-negative integers a1, a2, ..., an ,
    where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints
    of line i is at (i, ai) and (i, 0).
Output: the maximum possible area between any of the two lines

Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Runtime: O(n)

Example 1:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Example 2:
Input: [1,2,4,3]
Output: 4

Brute force: 
- Consider every pair of lines and find the area between every pair
- Runtime: O(n^2)

Two pointer method:
- area is width * height, so it's a trade off between the height of the lines
  and the distance b/w the lines
- left pointer starts at index 0
- right pointer starts at the last index
- at each iteration, the pointer at the smaller height moves inward by 1 b/c
  moving the pointer at the larger height will only decrease the area (the area
  is calculated by taking min{height[left], height[right]} and the width
  decreases by 1 every time you step inward)
- Runtime: O(n), Space complexity: O(1)
"""


def max_area(height):
    """
    Assume that n is at least 2.
    Start with the maximum width container, two pointer method
    """
    if len(height) < 3:
        return min(height)

    left = 0
    right = len(height) - 1
    maximum = 0
    while left < right:
        maximum = max(maximum, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maximum


assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert max_area([1, 2, 4, 3]) == 4
assert max_area([1, 2]) == 1
assert max_area([3, 2, 4]) == 6
assert max_area([1, 1, 1, 6, 6, 1]) == 6
