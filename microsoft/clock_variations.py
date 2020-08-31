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


def valid_times_alt(A, B, C, D):
    """
    Runtime: O(n!), Space complexity: O(n!) where n always equals 4 here
    """
    def get_permutation(str_list, start, end, perms):
        if start == end:
            hour = ''.join(str_list[:2])
            minutes = ''.join(str_list[2:])
            if ("00" <= hour < "24" and "00" <= minutes <= "59") or (hour == "24" and minutes == "00"):
                perms.add(hour + minutes)
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
    return len(permutations)


def valid_times_alt_alt(A, B, C, D):
    """
    Runtime: O(n!), Space complexity: O(n!) where n always equals 4 here
    """
    def get_permutation(str_list, start, end, perms):
        count = 0
        if start == end:
            time = ''.join(str_list)
            if time not in perms:
                hour = time[:2]
                minutes = time[2:]
                if ("00" <= hour < "24" and "00" <= minutes <= "59") or (hour == "24" and minutes == "00"):
                    perms.add(time)
                    count += 1
        else:
            for i in range(start, end):
                # swap start and i-th element
                str_list[start], str_list[i] = str_list[i], str_list[start]
                # reduce size of substring to get to sub-problems
                count += get_permutation(str_list, start + 1, end, perms)
                # backtrack, swap back to the previous configuration so that you can try other configurations from there
                str_list[start], str_list[i] = str_list[i], str_list[start]
        return count

    strings = [str(A), str(B), str(C), str(D)]
    return get_permutation(strings, 0, len(strings), set())


def test(function):
    assert function(1, 0, 0, 2) == 12
    assert function(2, 1, 2, 1) == 6
    assert function(1, 4, 8, 2) == 5
    assert function(4, 4, 4, 4) == 0


functions = [valid_times, valid_times_alt, valid_times_alt_alt]
for func in functions:
    test(func)
