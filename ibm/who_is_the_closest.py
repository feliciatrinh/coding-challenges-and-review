"""
See related Leetcode Shorted Distance to Target Color
Input: string s and integer array queries of size n
Output: an integer array of size n that denotes the answer of each query

queries[i] is a query. In each query, you are given an index a where 0 <= a < len(s) of a character in s.
In your answer array, answer[i] needs to be the index of the closest same character or -1 otherwise.
If there are multiple answers, return the smallest one.

Example
Input: s = 'babab', queries = [2]
Output: [0]

Ideas
- iterate through the string, keep a dictionary containing char, list of indices as key, value pairs
    - for each element in queries, iterate through dict[char] to find the prev occurrence and/or next occurrence if
      applicable and return the one with the smallest distance away from queries[i]
    - Runtime: O(M + N * M)? Space: O(M)
    - can keep a set of indices instead
        - make j = queries[i]
        - check if j - 1 in dict[char] set, then check if j + 1 in dict[char] set
        - then check if j - 2 or j + 2 in dict[char] and so on until you reach index 0 or index len(s) - 1

- go left and right from queries[i] to find the next index of the character, take the one with min distance away
    - runtime O(M * N), Space: O(1)
    - wouldn't be able to optimize like the previous solution by returning -1 when you know there's only one instance
      of a character
"""


def who_closest(s, queries):
    """
    Runtime: O(M + N * M), Space: O(M) where M is length of s and N is length of queries
    """
    char_to_indices = dict()
    for i, char in enumerate(s):
        if char in char_to_indices:
            char_to_indices[char].append(i)
        else:
            char_to_indices[char] = [i]

    answer = []
    for q in queries:
        char = s[q]
        indices = char_to_indices[char]
        if len(indices) == 1:
            answer.append(-1)
        else:
            closest = -1
            dist = len(s)
            for index in indices:
                if index == q:
                    continue
                if abs(index - q) < dist:
                    dist = abs(index - q)
                    closest = index
            answer.append(closest)
    return answer


def who_closest_alt(s, queries):
    """
    Runtime: O(M + N * M), Space: O(M) where M is length of s and N is length of queries
    """
    char_to_indices = dict()
    for i, char in enumerate(s):
        if char in char_to_indices:
            char_to_indices[char].add(i)
        else:
            char_to_indices[char] = {i}

    answer = []
    for q in queries:
        char = s[q]
        indices = char_to_indices[char]
        if len(indices) == 1:
            answer.append(-1)
        else:
            dist = 1
            while True:
                if q - dist in indices:
                    answer.append(q - dist)
                    break
                elif q + dist in indices:
                    answer.append(q + dist)
                    break
                dist += 1
    return answer


def test(function):
    assert function('hackerrank', [4, 1, 6, 8]) == [-1, 7, 5, -1]
    assert function('babab', [2]) == [0]
    assert function('aaaa', [0, 1, 2, 3]) == [1, 0, 1, 2]
    assert function('sam', [1]) == [-1]
    assert function('abaaa', [0, 2, 3, 4]) == [2, 3, 2, 3]


functions = [who_closest, who_closest_alt]
for func in functions:
    test(func)
