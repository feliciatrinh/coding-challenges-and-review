"""
Input: array avg that consists of 0's or 1's
Output: the minimum number of moves it takes to get all 0's on one side and all 1's on the other side

1 <= n <= 10^5

You can only swap two indices that are right next to each other and it counts as one move.

Example
Input: [0, 1, 0, 1]
Output: 1, swap students 1 and 2

Input: [1, 1, 1, 1, 0, 1, 0, 1]
Output: 3
swap indices 4 and 5, swap 6 and 7, swap 5 and 6

Ideas
- you always want to have a 0 and 1 switch with each other?
- you move all the 1's to the right starting from the last instance of 1 or move all the 1's to the left starting from
  the first 1 that appears in the array
    - keep track of the indices of every 1 in array
    - calculate the difference b/w this 1 and the beginning of the array to count the number of swaps
    - update the new start index to be start + 1
    - keep "swapping" the 1's to the left until you are out of 1
    - do the same process to swap the ones to the right and take the minimum number of swaps
    - runtime: O(N), Space: O(N)

    - a similar idea would be to count the number of zeros in between the left end and 1's then the number of zeros in
      b/w 1's and the right end. Then, take the minimum
    - runtime: O(N), Space: O(1)
"""


def min_moves(avg):
    """
    Runtime: O(N), Space: O(N)
    """
    one_indices = []
    for i, digit in enumerate(avg):
        if digit == 1:
            one_indices.append(i)

    left_moves = 0
    start = 0
    for i in one_indices:
        if i != start:
            left_moves += i - start
        start += 1

    right_moves = 0
    start = len(avg) - 1
    for i in one_indices[::-1]:
        if i != start:
            right_moves += start - i
        start -= 1
    return min(left_moves, right_moves)


def min_moves_alt(avg):
    """
    Runtime: O(N), Space: O(1)
    """
    num_zeros = 0
    left_moves = 0
    for digit in avg:
        if digit == 1:
            left_moves += num_zeros
        else:
            num_zeros += 1

    num_zeros = 0
    right_moves = 0
    for digit in avg[::-1]:
        if digit == 1:
            right_moves += num_zeros
        else:
            num_zeros += 1
    return min(left_moves, right_moves)


def test(function):
    assert function([0, 1, 0, 1]) == 1
    assert function([1, 1, 1, 1, 0, 0, 0, 0]) == 0
    assert function([0]) == 0
    assert function([1]) == 0
    assert function([1, 1, 1, 1, 0, 1, 0, 1]) == 3


functions = [min_moves, min_moves_alt]

for func in functions:
    test(func)
