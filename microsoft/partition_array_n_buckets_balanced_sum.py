"""
Input: a sorted array of integers and integer k
Output: list of k sub-arrays with approximately equal sums

Example
Input: [1, 2, 3, 4, 5], k = 3
Output: [[5], [1, 4], [2, 3]]

- we want the sum of each sub-array to be as close to sum(array) // k as possible?
"""


def partition(arr, k):
    """
    Runtime: O(), Space: O()
    """

