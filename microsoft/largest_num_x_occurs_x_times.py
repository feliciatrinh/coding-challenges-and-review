"""
Input: array A
Output: the biggest value X which occurs in A exactly X times, or 0 otherwise

A consists of N integers where N in range [1, 10^5]
each element of A is an integer in range [1, 10^9]

Example
Input: A = [3, 8, 2, 3, 3, 2]
Output: 3

Input: A = [7, 1, 2, 8, 2]
Output: 2

Input: A = [3, 1, 4, 1, 5]
Output: 0

Input: A = [5, 5, 5, 5, 5]
Output: 5

Ideas
- if there's an element of A that is > 10^5 then return 0 b/c a single element can appear in A at most 10^5 times
- keep track of frequency of each element in a dictionary
- once done with building the dictionary, iterate through each key, value pair
    - if key == value, then update the biggest value X
"""


def largest_x_num(A):
    """
    Runtime: O(N), Space complexity: O(N)
    """
    freq = dict()
    for a in A:
        if a in freq:
            freq[a] += 1
        else:
            freq[a] = 1

    max_num = 0
    for num, count in freq.items():
        if num == count:
            max_num = max(max_num, num)
    return max_num


assert largest_x_num([3, 8, 2, 3, 3, 2]) == 3
assert largest_x_num([7, 1, 2, 8, 2]) == 2
assert largest_x_num([3, 1, 4, 1, 5]) == 0
assert largest_x_num([5, 5, 5, 5, 5]) == 5
assert largest_x_num([4]) == 0
