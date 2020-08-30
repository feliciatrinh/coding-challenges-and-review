"""
Input: integer array cars and integer k
Output: minimum length of a roof that can cover k cars

1 <= k <= n
1 <= cars[i] <= 10^14
all slots taken by cars are unique

Example
Input: cars = [2, 10, 8, 17], k = 3
Output: 9

Input: cars = [1, 2, 3, 10], k = 4
Output: 10

Ideas
- sort cars in O(NlogN) time
    - for every k length window, calculate the roof length and take the minimum
    - roof length is high - low + 1
    - Runtime: O(NlogN) + O(N) = O(NlogN), Space: O(1) if you sort cars in-place
- if k == len(cars) then you have to cover all cars. roof length has to be max - min + 1
    - runtime: O(N), Space: O(1)
"""


def parking_dilemma(cars, k):
    """
    Runtime: O(NlogN), Space: O(1)
    """
    if k == len(cars):
        return max(cars) - min(cars) + 1

    cars.sort()
    min_roof = max(cars) - min(cars) + 1
    for i in range(len(cars) - k + 1):
        min_roof = min(min_roof, cars[i + k - 1] - cars[i] + 1)
    return min_roof


assert parking_dilemma([2, 10, 8, 17], 3) == 9
assert parking_dilemma([1, 2, 3, 10], 4) == 10
assert parking_dilemma([9, 20, 13, 11], 2) == 3

