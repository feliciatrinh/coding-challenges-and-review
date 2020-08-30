"""
Input: array A representing coordinates of N points, integer M
Output: size of the largest M-aligned subset of the given N points

- N points are on a line, coordinates of these points are in A
- coordinates do not need to be distinct
- a subset of these points is M-aligned if the distance b/w any 2 points w/in the subset is divisible by M

Example
Input: A = [-3, -2, 1, 0, 8, 7, 1], M = 3
Output: 4
The 3-aligned subset contain the 4 points at -2, 1, 7, 1
- b/c dist b/w -2 and 1 is 3 -> 2 of these
- dist b/w each 1 and 7 is 6 -> 2 of these
- dist b/w -2 and 7 is 9 -> 1 of these

Idea
- order the coordinates from least to greatest
- start from the left and go forward like top sort?
- for each coordinate, see if there's a point M units away then keep jumping forward until you can't anymore
    - then see if there's a point M * 2 units away and keep jumping and so on?
    - runtime: O(n^2)?

- can i keep a dictionary mapping coordinate to number of points that lie there?
  e.g. {-3: 1, -2: 1, 1: 2, 0: 1, 8: 1, 7: 1}
- keep track of the maximum coordinate and min coord as you throw the points into the dictionary
- start from either the max coord or the min coord, let's say we start from the min coord
    - keep track of max number of points in subsets seen so far
    - count how many points are +M units away, then +2M units away, then +3M units away until
      min_coord + c * M > max_coord for some constant c
    - update max_num_points
    - then move onto the point after the min_coord and repeat
    - keep repeating this until you get to a point whose coord is >= min_coord b/c you would have already looked at the
      points beyond this
- Runtime: O(N) for adding to dictionary + O(M * (max_coord - min_coord) // M) for checking the points and counting?

Source: Leetcode
- form groups of M-aligned numbers like grouping together coords with the same remainder
example: A = [-3, -2, 1, 0, 8, 7, 1], M = 3
         r = [0, 1, 1, 0, 2, 1, 1] where r is the remainder aka r[i] = A[i] % m
- difference of any two numbers with the same remainder after dividing by M is guaranteed to be divisible by M
  if i % m == j % m then (i - j) % m == 0
- so our subsets are [-3, 0], [-2, 1, 7, 1], [8]
- group 2 is the largest so we return 4
"""


def largest_subset_best(A, M):
    """
    Runtime: O(N), Space complexity: O(M)
    """
    if not A or M <= 0:
        return 0

    remainder_to_count = dict()
    max_count = 0
    for coord in A:
        remainder = coord % M
        if remainder not in remainder_to_count:
            remainder_to_count[remainder] = 1
        else:
            remainder_to_count[remainder] += 1
        max_count = max(max_count, remainder_to_count[remainder])
    return max_count


def largest_subset(A, M):
    """
    First attempt
    Runtime: O(N) + O(M * (max_coord - min_coord) // M)
    Space: O(N)
    """
    if not A or M <= 0:
        return 0

    coord_to_count = dict()
    max_coord = A[0]
    min_coord = A[0]
    for coord in A:
        if coord not in coord_to_count:
            coord_to_count[coord] = 1
        else:
            coord_to_count[coord] += 1
        max_coord = max(max_coord, coord)
        min_coord = min(min_coord, coord)

    # subsets = []
    max_points = 0
    for i in range(M):
        curr_points = 0
        curr_coord = min_coord + i
        if curr_coord in coord_to_count:
            curr_points += coord_to_count[curr_coord]
            # subsets.append([curr_coord])
        else:
            continue
        # jump at most (max_coord - min_coord) // M times
        for _ in range((max_coord - min_coord) // M):
            curr_coord += M
            if curr_coord in coord_to_count:
                curr_points += coord_to_count[curr_coord]
                # if you want to see the subsets
                # subsets[i].append(curr_coord)
        max_points = max(max_points, curr_points)
    return max_points


assert largest_subset([-3, -2, 1, 0, 8, 7, 1], 3) == 4
assert largest_subset([-3, -2, 1, 0, 8, 7, 1], 2) == 4
assert largest_subset([-3, -2, 1, 0, 8, 7, 1], 1) == 7
assert largest_subset([1, 4], 2) == 1

assert largest_subset_best([-3, -2, 1, 0, 8, 7, 1], 3) == 4
assert largest_subset_best([-3, -2, 1, 0, 8, 7, 1], 2) == 4
assert largest_subset_best([-3, -2, 1, 0, 8, 7, 1], 1) == 7
assert largest_subset_best([1, 4], 2) == 1
