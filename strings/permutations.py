def permutations(s):
    """
    Given string s with distinct characters, return list of all possible permutations of s
    Finds all permutations of the s[0:len(s)-1] then inserts the last character into every possible
    location in each permutation
    O(n * n!) runtime

    can print all permutations by [print(p) for p in permutations(s)]
    """
    if len(s) <= 1:
        return [s]
    perms = permutations(s[:len(s)-1])
    last = s[-1]
    all_perms = []
    for p in perms:
        # last char can be inserted at the beginning, anywhere in the middle, at end
        for i in range(len(p) + 1):
            all_perms.append(p[:i] + last + p[i:])
    return all_perms


def permutations_alt(s):
    """
    Backtracking solution
    Reduce the size of each substring to solve the sub-problems then backtrack to get another permutation from that
    section.
    Runtime: O(n!)
    """
    def get_permutation(str_list, start, end, perms):
        if start == end:
            perms.append(''.join(str_list))
        else:
            for i in range(start, end):
                # swap start and i-th element
                str_list[start], str_list[i] = str_list[i], str_list[start]
                # reduce size of substring to get to sub-problems
                get_permutation(str_list, start + 1, end, perms)
                # backtrack
                str_list[start], str_list[i] = str_list[i], str_list[start]
        return perms

    str_list = list(s)
    return get_permutation(str_list, 0, len(s), [])


print(permutations_alt("ABC"))
