# Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the arr element between
# two given indices, inclusive. Once all operations have been performed, return the max value in your array.
# runtime O(num operations + length array)? 
# solution achieved after reading discussion board in hackerrank

def arrayManipulation(n, queries):
    arr = [0]*n
    for row in queries:
        left = row[0] - 1
        right = row[1]
        k = row[2]
        arr[left] += k
        # if you add k to every element in arr then the difference between each element remains the same
        if right != len(arr):
            arr[right] -= k
    maximum = 0
    diffs = 0
    # add up the differences, maximum is the sum of the positive differences
    for item in arr:
        diffs += item
        if maximum < diffs: 
            maximum = diffs
    return maximum
