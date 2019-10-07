"""
Input: 2D array of operations
Output: Maximum value in array as a long int

Starting with a 1-indexed array of zeros and a list of operations, 
for each operation add a value to each of the arr elements between
two given indices, inclusive. Once all operations have been performed, 
return the max value in your array.

Runtime O(num operations + length array)

example
a  b  k
1  2  10
2  3  15
3  4  2
1  6  14
5  6  3

returns 39
"""


def arrayManipulation(n, queries):
    arr = [0]*n
    for row in queries:
        left = row[0] - 1
        # you don't subtract 1 from right because this index is 1 spot after b
        # the value at this index represents the difference between the current element and the previous element
        right = row[1]
        k = row[2]
        arr[left] += k
        # if you add k to every element in arr then the difference between each element remains the same
        if right != len(arr):
            arr[right] -= k
    maximum = 0
    diffs = 0
    # add up the differences from left to right
    # solution is the maximum running sum you achieve
    for item in arr:
        diffs += item
        if maximum < diffs: 
            maximum = diffs
    return maximum
