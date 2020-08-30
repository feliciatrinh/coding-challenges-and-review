"""
Input: array A of N integers
Output: max sum of two numbers whose digits add up to an equal sum or -1 otherwise

N w/in range [1, 200000]
Each element in array w/in range [1, 10^9]

Example
Input: [51, 71, 17, 42]
Output: 93
The numbers whose digits add up to an equal sum of 8 are 71 and 17.
Nums whose digits add up to equal sum of 6 are 51 and 42.
71 + 17 = 88
51 + 42 = 93 so the max is 93

Input: [42, 33, 60]
Output: 102
All nums have digits that add up to 6
42 + 33 = 75
42 + 60 = 102
33 + 60 = 93

Input: [51, 32, 43]
Output: -1
No pair of nums whose digits have the same sum

Ideas
Input: [41, 32, 50], Output: 91
- keep a dictionary mapping digit sum to numbers (e.g. {5: 41})
- as you iterate through array A, check if it's digit sum is in the dictionary
    - if present, set the running max accordingly and update the dictionary value to max {old_value, current_num}
"""


def max_sum(A):
    """
    Runtime: O(n), Space complexity: sub-linear?
    Maximum digit sum we can have is 81?
    """
    def get_digit_sum(x):
        result = 0
        while x != 0:
            result += x % 10
            x = x // 10
        return result

    maximum_sum = -1
    digit_sum_to_num = {}
    for num in A:
        digit_sum = get_digit_sum(num)
        if digit_sum in digit_sum_to_num:
            maximum_sum = max(maximum_sum, num + digit_sum_to_num[digit_sum])
            digit_sum_to_num[digit_sum] = max(digit_sum_to_num[digit_sum], num)
        else:
            digit_sum_to_num[digit_sum] = num
    return maximum_sum


assert max_sum([51, 71, 17, 42]) == 93
assert max_sum([42, 33, 60]) == 102
assert max_sum([51, 32, 43]) == -1
