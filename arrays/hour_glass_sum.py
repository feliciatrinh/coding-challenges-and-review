"""
Source: hackerrank
Input: 2D array
Output: the maximum hourglass sum in the array
"""


def hourglass_sum(arr):
    sums = []
    for row in range(len(arr) - 2): 
        for col in range(len(arr[0]) - 2): 
            sum = 0
            for j in range(col, col + 3): 
                sum += arr[row][j]
                sum += arr[row + 2][j]
            sum += arr[row + 1][col + 1]
            sums.append(sum)
    return max(sums)
