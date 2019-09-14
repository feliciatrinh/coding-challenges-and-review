"""
returns the maximum difference between elements nums[j] and nums[i]
where j > i
returns -1 if there is no such difference
runtime O(n)?
"""

def maxDifference(nums):
    # if array is sorted from greatest to least, return -1
    # naive solution is to compare between every element
    # better solution is to keep track of the minimum element that's before num[j]
    length = len(nums)
    min_num = nums[0]
    max_diff = -1
    for j in range(1, length-1): 
        curr_diff = nums[j] - min_num
        if (curr_diff > max_diff): 
            max_diff = curr_diff
        if nums[j] < min_num: 
            min_num = nums[j] # if the current element is smaller than the curr minimum
    return max_diff
    
