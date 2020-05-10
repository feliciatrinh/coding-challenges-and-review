"""
Input: an array A of integers
Output: longest increasing subsequence (LIS) in terms of length

Example 1:
Input: [11, 100, 1, 7, 18, 23, 25, 10]
Output: [1, 7, 18, 23, 25]

Idea:
- Can create a DAG out of these with edges i -> j if A[i] < A[j]
- The longest increasing subsequence is the longest path in this DAG
    - To solve longest path in a DAG, we find the longest path that ends at
      each node starting with the first node

Subproblem:
- L(i) is the length of the longest increasing subsequence that ends at index i

Recurrence relation:
- L(i) = max {L(j) + 1, L(i)} for all j -> i edges which are incoming edges
  into node i

Algorithm:
- Solve in increasing order of i
- Keep a prev array where prev[i] = j for which the maximum length is attained
- last index of the LIS (called last_index) is argmax{L(1), L(2), ..., L(n)}
- step backwards through prev array starting from last_index, these are the
  indices of the LIS

Runtime: O(n^2) b/c runtime is the number of edges
But a O(nlogn) solution exists.
"""


def longest_increasing_subsequence(arr):
    def construct_DAG(arr):
        """
        Construct a dictionary adjacency list representation of the DAG
        There's an edge j -> i is A[j] < A[i]
        Runtime: O(n^2) for number of edges
        """
        graph = {i: [] for i in range(len(arr))}
        for i in range(len(arr)):
            for j in range(0, i):
                if arr[j] < arr[i]:
                    graph[i].append(j)
        return graph

    if len(arr) < 2:
        return arr

    graph = construct_DAG(arr)
    # contains length of LIS ending at index i
    L = [1] * len(arr)

    # prev[i] = j for which the maximum length is attained
    prev = [-1] * len(arr)
    # keep track of the global maximum so we can keep track of the last node
    longest_len = 1
    last_index = 0
    for i in range(len(arr)):
        for j in graph[i]:
            # L(i) = max {L(j) + 1, L(i)} for all j -> i
            if L[j] + 1 > L[i]:
                L[i] = L[j] + 1
                prev[i] = j
            if L[i] > longest_len:
                longest_len = L[i]
                last_index = i

    # step backwards through prev starting from the index of the last element
    # in the LIS
    result = []
    while last_index != -1:
        result.insert(0, arr[last_index])
        last_index = prev[last_index]
    return result


assert longest_increasing_subsequence([11, 100, 1, 7, 18, 23, 25, 10]) == [1, 7, 18, 23, 25]
assert longest_increasing_subsequence([2, 3, 4, -3, -5, 100]) == [2, 3, 4, 100]
assert longest_increasing_subsequence([1]) == [1]
assert longest_increasing_subsequence([1, -4]) == [1]
assert longest_increasing_subsequence([10,9,2,5,3,7,101,18]) == [2, 5, 7, 101]
