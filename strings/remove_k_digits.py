"""
Source: Leetcode
Input: non-negative integer num represented as a string and integer k
Output: num with k digits removed such that the new number is the smallest possible

length of num is less than 10002 and >= k
given num does not contain leading zeros
Output must not contain leading zeros

Example
Input: num = "1432219", k = 3
Output: "1219"

Input: num = "10200", k = 1
Output: "200"

Input: num = "10", k = 2
Output: "0"

Ideas
- I know doing int('002') will get rid of the leading zeros and return 2, then I could return the string by doing str(2)
- brute force: remove a digit at index 0 then recursively remove_k_digits(new_num, k - 1) and so on for all indices 0
  through len(num) - 1. Then, return the minimum num

- scan from right to left and remove that digit when it's greater than the next digit and repeat k times
  e.g. in "102", we'll remove 1 because it's greater than 0
"""


def remove_k_digits_naive(num, k):
    """
    Runtime: O(factorial?, exponential?), Space: O(N)
    """
    if num == "":
        return "0"
    if k == 0:
        return num

    res = set()
    for i in range(len(num)):
        new_num = num[:i] + num[i + 1:]
        if not new_num:
            res.add(0)
        elif int(new_num) not in res:
            res.add(int(remove_k_digits_naive(new_num, k - 1)))
    return str(min(res))


def remove_k_digits(num, k):
    """
    Runtime: O(N + k), Space: O(1)
    k <= N so runtime is O(N)?
    """
    i = 0
    while num and k > 0:
        if i != 0:  # if this if condition was changed to 'i = 0' then runtime would be O(N * k)
            # move the curr character pointer to the character that comes right before the last character you removed
            i -= 1
        while i < len(num) - 1 and num[i] <= num[i + 1]:
            i += 1
        num = num[:i] + num[i + 1:]
        k -= 1

    # removes leading zeros
    num = num.lstrip("0")
    if not num:
        return "0"
    return num


def remove_k_digits_alt(num, k):
    """
    Runtime: O(N + k)?, Space: O(N)
    """
    keep = []
    for char in num:
        while keep and keep[-1] > char and k > 0:
            keep.pop()
            k -= 1
        keep.append(char)

    # k could be nonzero at this point
    res = "".join(keep[:len(keep) - k])
    # removes leading zeros
    res = res.lstrip("0")
    if not res:
        return "0"
    return res


def test(function):
    assert function("1432219", 3) == "1219"
    assert function("10200", 1) == "200"
    assert function("10", 2) == "0"
    assert function("", 0) == "0"
    assert function("54321", 2) == "321"
    assert function("12345", 3) == "12"
    assert function("50102040", 4) == "0"
    assert function("10012", 2) == "1"


functions = [remove_k_digits, remove_k_digits_alt]

for f in functions:
    test(f)
