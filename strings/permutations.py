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
