"""
Input: a string s and costs
Output: minimum total cost of deletions needed to achieve a string without two identical consecutive letters.

The costs remain the same even as you delete.
Assumptions
- s and costs have length equal to N
- N in range [1, 10^5]
- s consists only of lowercase letters
- each element of costs is an integer w/in range [0, 1000]

Example
Input: s = "abccdb", costs = [0, 1, 2, 3, 4, 5]
Output: 2
Delete the first occurrence of 'c' for a cost of costs[2] = 2

Input: s = "aabbcc", costs = [1, 2, 1, 2, 1, 2]
Output: 3
Delete all letters with cost 1

Input: s = "aaaa", costs = [3, 4, 5, 6]
Output: 12
3 + 4 + 5 = 12

Input: s = "ababa", costs = [10, 5, 10, 5, 10]
Output: 0

Ideas
- recursive solution
- iterate through the string
    - check if curr_char == prev_char, if so then delete either the prev_char or the curr_char by adding to the running
      cost
    - keep track of the running cost and the min_cost
    - keep track of the current index and the prev_char as you recurse
- runtime is at most summation 2^i where i is 0 to n - 1? = 2^(n + 1) - 1 so runtime O(2^n)?

- dynamic programming?
- subproblem: M(i) is minimum cost of deleting letters up index i
- Recurrence relation: M(i) = min { M(i - 1) + costs[i - 1], M(i - 1) + costs[i] } if s[i - 1] == s[i]
  the minimum b/w deleting the prev char or deleting the current character
- Base case: M(i) = 0 if i == 0
- final answer M(len(s) - 1)
- Runtime: O(n), Space: O(n)

- as you iterate through the string, if you choose to delete at the current index, you have to replace this index's cost
  with the cost of the prev index b/c of cases like "adddd"

Best solution
- or you can keep track of the prev cost to consider instead of changing the costs array
"""


def min_cost(s, costs):
    """
    Runtime: O(2^n), Space complexity: O(n)
    """
    def get_cost(index, prev_char):
        """
        Returns the minimum cost b/w deleting the character at the previous index or deleting the character at the
        current index.
        """
        if index < 0 or index > len(s) - 1:
            return 0
        if s[index] == prev_char:
            cost = min(costs[index - 1], costs[index])
            if costs[index] < costs[index - 1]:
                costs[index] = costs[index - 1]
            return get_cost(index + 1, prev_char) + cost
        else:
            return get_cost(index + 1, s[index])

    return get_cost(0, '')


def min_cost_dp(s, costs):
    """
    Runtime: O(n), Space complexity: O(n)
    """
    M = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cost = min(costs[i - 1], costs[i])
            if costs[i] < costs[i - 1]:
                costs[i] = costs[i - 1]
            M[i] = M[i - 1] + cost
        else:
            M[i] = M[i - 1]
    return M[len(s) - 1]


def min_cost_alt(s, costs):
    """
    Runtime: O(n), Space complexity: O(1)
    """
    total_cost = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cost = min(costs[i - 1], costs[i])
            if costs[i] < costs[i - 1]:
                costs[i] = costs[i - 1]
            total_cost += cost
    return total_cost


def min_cost_alt_alt(s, costs):
    """
    Runtime: O(n), Space: O(1)
    Instead of changing the costs array, I could keep track of the prev index that I use for cost comparisons.
    The j-th character is an earlier duplicate that I haven't deleted.
    The i-th character is the current character I am considering deleting.
    """
    total_cost = 0
    j = 0  # our prev index
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            # delete the i-th character
            if costs[i] < costs[j]:
                cost = costs[i]
                j = i - 1
            # delete the j-th character (which comes before i)
            else:
                cost = costs[j]
                j = i
            total_cost += cost
        else:
            j += 1
    return total_cost


def test(function):
    assert function("abccdb", [0, 1, 2, 3, 4, 5]) == 2
    assert function("aabbcc", [1, 2, 1, 2, 1, 2]) == 3
    assert function("aaaa", [3, 4, 5, 6]) == 12
    assert function("ababa", [10, 5, 10, 5, 10]) == 0
    assert function("a", [10]) == 0
    assert function("adddd", [0, 6, 2, 8, 9]) == 16
    assert function('abccccce', [1, 2, 4, 3, 6, 2, 1, 1]) == 10


functions = [min_cost, min_cost_dp, min_cost_alt, min_cost_alt_alt]
for func in functions:
    test(func)
