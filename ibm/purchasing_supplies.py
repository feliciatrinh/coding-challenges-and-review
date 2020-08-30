"""
Input: integer budget n, unit cost of container, integer number of empty containers to return for a free container m
Output: maximum number of empty containers a customer can receive

1 <= n <= 10^3
2 <= budget <= 10^5
1 <= cost of container <= budget
2 <= number of empty containers to return <= budget

Ideas
- need to keep track of total containers over time and curr number of containers
- always spend entire budget on containers initially
- calculate how many you can receive for trading in using floor
"""


def purchasing_supplies(n, cost, m):
    """
    Runtime: O(logN), Space: O(1)
    """
    curr_count = n // cost
    total_count = n // cost
    while curr_count >= m:
        # amount of containers you receive when you trade in
        receive = curr_count // m
        total_count += receive
        # curr_count = curr_count - receive * m + receive
        # curr_count = curr_count - receive * (m - 1)
        # can also write curr_count = curr_count % m and then curr_count += receive
        curr_count -= receive * (m - 1)
    return total_count


assert purchasing_supplies(4, 1, 2) == 7
assert purchasing_supplies(10, 2, 5) == 6
assert purchasing_supplies(12, 4, 4) == 3
assert purchasing_supplies(6, 2, 2) == 5
assert purchasing_supplies(5, 5, 2) == 1
assert purchasing_supplies(8, 4, 2) == 3
assert purchasing_supplies(7, 2, 3) == 4
