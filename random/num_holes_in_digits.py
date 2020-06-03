"""
Input: integer num (assuming input can be positive or negative)
Output: number of holes in that number

Runtime: O(n), linear in the number of digits in number.
Space complexity: O(1)?
- Uses additional memory for the digits_to_closed_paths dictionary, though its size is independent of the input.
"""


def num_holes(num):
    if num == 0:
        return 1

    digit_to_holes = {0: 1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 1, 7: 0, 8: 2, 9: 1}

    holes = 0
    num = abs(num)
    while num > 0:
        digit = num % 10
        holes += digit_to_holes[digit]
        num = num // 10
    return holes


def num_holes_alt(num):
    if num == 0:
        return 1

    holes = 0
    num = abs(num)

    while num > 0:
        digit = num % 10
        if digit in set(0, 4, 6, 9):
            holes += 1
        elif digit == 8:
            holes += 2
        num = num // 10
    return holes


assert num_holes(6457819) == 5
assert num_holes(0) == 1
assert num_holes(1235732) == 0
assert num_holes(-7462039587) == 6
