"""
See related Three Sum Smaller
Input: array of n distinct integers d and integer threshold t
Output: number of (a, b, c) index triplets that satisfy d[a] < d[b] < d[c] and d[a] + d[b] + d[c] <= t

1 <= n <= 10^4
0 <= d[i] < 10^9
0 < t < 3 * 10^9

Example
Input: [1, 2, 3, 4, 5], t = 8
Output: 4
(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4)

Ideas
- similar to the 3 sum problem?
- n integers are distinct, so you can form a pair then check for a satisfying third number
- if I sort it first, runtime would be O(NlogN) + O(N^2)?
    - if I find that d[i] + d[i + 1] + d[i + 2] > t  where d is sorted then i can stop iterating through d and return
    - if max(d) * 3 > t then all possible triplets in d satisfy the conditions, so len(d) choose 3 triplets?
        - if the sum of the last three elements after sorting are >= t then all possible triplets will work
        - optional condition, totally not needed especially if you don't want imports (works with python 3.8)
    - if d[0] + d[1] + d[2] = k < t then I can have a delta variable where delta is at first 0 then increment by 1
      until the current triple sum + delta >= t

Example: Input after sorting is [1, 2, 3, 4, 5], t = 8
k is at first 1 + 2 + 3 = 6 < 8 and delta = 0
- We keep 1 and search the rest of the array for two numbers that sum to k - d[0] + delta = 6 - 1 + 0 = 5
- then we find two numbers in array[2:] that sum to 6 then two numbers in array[3:] that sum to 7 then 8 then stop
- 2 + 3 + 4 = 9 > 8 so we stop
- otherwise we would keep 2 and search the rest of the array for two numbers that sum to 9 - 2 + delta where delta is
  again 0
"""


def triplets(d, t):
    """
    First attempt
    Runtime: O(NlogN + N^3) = O(N^3), Space: O(N)
    """
    def two_sum(nums, target):
        """
        Runtime: O(N), Space: O(N)
        """
        if sum(nums[-2:]) < target:
            return 0

        seen = set()
        count = 0
        for j in nums:
            complement = target - j
            if complement in seen:
                count += 1
            seen.add(j)
        return count

    if len(d) < 3:
        return 0

    d.sort()
    num_triplets = 0
    for i, num in enumerate(d):
        k = sum(d[i: i + 3])
        if k > t or i > len(d) - 3:
            break

        delta = 0
        while k + delta <= t:
            num_triplets += two_sum(d[i + 1:], k - num + delta)
            delta += 1
    return num_triplets


def triplets_better(d, t):
    """
    Runtime: O(NlogN) + O(N^2) = O(N^2), Space: O(N)
    """
    def two_sum_smaller(nums, target):
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] <= target:
                count += 1
                left += 1
            else:
                right -= 1
        return count

    if len(d) < 3:
        return 0

    d.sort()
    num_triplets = 0
    for i, num in enumerate(d):
        if i > len(d) - 3:
            break
        num_triplets += two_sum_smaller(d[i + 1:], t - num)
    return num_triplets


def test(function):
    assert function([1, 2, 3, 4, 5], 8) == 4
    assert function([1, 2, 3, 4], 12) == 4
    assert function([5, 4, 2], 1) == 0
    assert function([10, 9], 9) == 0
    assert function([8, 7, 6, 5, 4, 3, 2, 1], 12) == 22


functions = [triplets, triplets_better]
for func in functions:
    test(func)
