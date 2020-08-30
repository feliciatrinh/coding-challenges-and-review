"""
Input: integers A, B, C, D
Output: number of valid 24-hour, digital clock format times you can form using these 4 integers

Given 4 integers, return how many valid times you can form using these 4 integers.
Valid times are between 00:00 and 24:00 (inclusive?? isn't 00:00 and 24:00 the same thing?)

A, B, C, D are integers b/w [0, 9]

Example
Input: 1, 0, 0, 2
Output: 12
(00:12) (00:21) (01: 02) (01:20) (02:10) (02:01) (10:02) (10:20) (12:00) (20:01) (20:10) (21:00)

Input: 2, 1, 2, 1
Output: 6
(21:21) (12:12) (21:12) (12:21) (11:22) (22:11)

Input: 1, 4, 8, 2
Output: 5
(14:28) (18:42) (18:24) (12:48) (21:48)

Input: 4, 4, 4, 4
Output: 0

Brute force
- form all permutations of hours and minutes possible
    - check each permutation if hours are b/w 00 and 24, check if minutes are b/w 00 and 59
    - there are 4 * 3 * 2 = 24 permutations possible?
    - can use itertools.permutations
    - can find all permutations possible by using backtracking
"""


def valid_times(A, B, C, D):
    """
    Runtime: O(n!), Space complexity: O(n!) where n always equals 4 here
    """
    def get_permutation(str_list, start, end, perms):
        if start == end:
            perms.add(''.join(str_list))
        else:
            for i in range(start, end):
                # swap start and i-th element
                str_list[start], str_list[i] = str_list[i], str_list[start]
                # reduce size of substring to get to sub-problems
                get_permutation(str_list, start + 1, end, perms)
                # backtrack
                str_list[start], str_list[i] = str_list[i], str_list[start]
        return perms

    strings = [str(A), str(B), str(C), str(D)]
    permutations = get_permutation(strings, 0, len(strings), set())
    count = 0
    for perm in permutations:
        hour = perm[:2]
        minutes = perm[2:]
        if "00" <= hour < "24" and "00" <= minutes <= "59":
            count += 1
        elif hour == "24" and minutes == "00":
            count += 1
    return count


assert valid_times(1, 0, 0, 2) == 12
assert valid_times(2, 1, 2, 1) == 6
assert valid_times(1, 4, 8, 2) == 5
assert valid_times(4, 4, 4, 4) == 0
