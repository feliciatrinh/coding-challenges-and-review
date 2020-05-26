"""
Input: array arr containing integers
Output: the number of subarrays in arr that contain m odd numbers

Runtime: O(n)

Naive
- create all possible subarrays
- go through each subarray and keep track of how many have m odd number

Better
- While iterating through the array, keep track of the number of subarrays in the part of the array where we haven't
  satisfied the number of odd numbers (the number of subarrays with only i odd numbers so far)
- keep track of this because you can add it on later since each additional even number makes a different subarray
""" 


def beautiful_subarrays(arr, m):
    num_subarrays = 0
    odd_elems = 0
    subarrays_so_far = [0] * len(arr) 
    # subarrays_so_far[i] is number of subarrays with i odd numbers
    for num in arr:
        subarrays_so_far[odd_elems] += 1
        # add to odd counter to move along the subarrays_so_far array
        if num % 2 != 0:
            odd_elems += 1

        # Don't increment the count if you have enough odd nums
        if odd_elems >= m:
            num_subarrays += subarrays_so_far[odd_elems - m]
            # if you have too many odd numbers, then you ignore the front portion of the array
            # and keep forming subarrays in the later parts of the array
    return num_subarrays
