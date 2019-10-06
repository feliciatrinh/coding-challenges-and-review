def sum_to_k(arr, k):
    """
    Given an array of integers (doesn't have to be distinct), return the number
    of pairs that sum to k
    Average runtime O(n), dictionary lookup and add should be similar to hash table? 
    and we iterate through the arr only twice
    """
    freq = {}
    for elem in arr: 
        if elem in freq:
            freq[elem] += 1
        else: 
            freq[elem] = 1
    count = 0 # counter for number of pairs
    for elem in arr: 
        if k - elem in freq: 
            # if the pair consists of the same numbers e.g. (1, 1)
            if k - elem == elem: 
                # to not count the element and itself as a pair                    
                count += freq[k - elem] - 1 
            else: 
                count += freq[k - elem]
    # divide count by 2 because we double-counted when iterating through the list 
    # is there a way to avoid double counting? 
    return count / 2   

# arr = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
# arr2 = [1, 1, 1, 1, -1, 3]
# sum_to_k(arr, 11) should return 9
# sum_to_k(arr2, 2) should return 7

def bad_sum_to_k(arr, k):
    """
    Given an array of integers, return the number of pairs that sum to k. 
    Average runtime O(n), worst case runtime O(n^2). 
    This solution doesn't work because it pairs the element up with itself
    i.e. it cannot distinguish the element in the set as itself
    """
    unique = set()
    for elem in arr: 
        unique.add(elem)
    count = 0
    for elem in arr: 
        if k - elem in unique: 
            count += 1
    return count
