"""
Input: two arrays A, B consisting of M integers each and an integer N, where A[i] and B[i] are cities at the two ends of
       the ith road
Output: maximal network rank in the whole infrastructure

Infrastructure consists of N cities numbered from 1 to N with M bidirectional roads b/w them.
Roads don't intersect apart from their start and end points.

For each pair of cities directly connected by a road, define their network rank as the total num of roads that are
connected to either of the two cities.

Example
Input: A = [1, 2, 3, 3], B = [2, 3, 1, 4], N = 4
Output: 4
Chosen cities could be 2 and 3. Four roads connected to them are (2, 1), (2, 3), (3, 1), (3, 4)

Idea
- create an adjacency list representation of cities mapped to roads connected to them
  ex: {1: {2, 3}, 2: {1, 3}, 3: {1, 2, 4}, 4: {3}}
- space complexity: O(M + N)
- iterate through each city, form pairs with cities they are connected to and keep track of pairs formed so far
    - for each pair, add the number of edges connected to each city in the pair to the current rank
        - subtract 1 to account for double counting
    - keep a running max and update as you go through each pair
    - Runtime:O(M) + O(NM)? O(M) for creating the infrastructure adjacency list, O(NM) for iterating through each city
      and its neighbors?

- I'm assuming you can't have any self edges and you will always have a valid N
"""


def max_network_rank(A, B, N: int) -> int:
    """
    Runtime: O(M) + O(NM)?, Space complexity: O(N + M)
    """
    infra = {i: set() for i in range(1, N + 1)}
    for j in range(len(A)):
        infra[A[j]].add(B[j])
        infra[B[j]].add(A[j])

    pairs = set()
    max_rank = 0
    for city, neighbors in infra.items():
        for neighbor in neighbors:
            rank = 0
            if (city, neighbor) in pairs or (neighbor, city) in pairs:
                continue
            else:
                pairs.add((city, neighbor))
                rank += len(infra[city]) + len(infra[neighbor]) - 1
                max_rank = max(max_rank, rank)
    return max_rank


assert max_network_rank([1, 2, 3, 3], [2, 3, 1, 4], 4) == 4
assert max_network_rank([1, 2, 3, 4], [2, 3, 4, 5], 5) == 3
assert max_network_rank([1, 2, 3, 4, 1, 2], [2, 4, 4, 1, 3, 3], 4) == 5
assert max_network_rank([1], [2], 3) == 1
