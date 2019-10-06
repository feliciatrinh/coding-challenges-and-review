    # returns number of subarrays in arr containing m odd numbers
    def beautifulSubarrays(arr, m):
    # Naive: creating all possible sub arrays then going through each one to see which
    # are beautiful would take too long
    # Better: when going through the array, keep track of num_subarrays in the part of the     
    # array where we haven't satisfied the num of odd elements yet 
    # so you can add it on later because each additional even element makes a different        
    # subarray
    # keep track of the num of sub arrays where you meet the odd num req and add it to the
    # above count
    num_subarrays = 0
    odd_elems = 0
    subarrays_so_far = [0] * len(arr) 
    # subarrays_so_far[i] is number of subarrays with i odd numbers
    for num in arr: 
        subarrays_so_far[odd_elems] += 1 
        if num % 2 != 0: # add to odd counter to move along the subarrays_so_far array
            odd_elems += 1
        if odd_elems >= m: # if you have enough odd nums
        # you don't increment the count
            num_subarrays += subarrays_so_far[odd_elems - m]
            # if you have too many odd numbers, then you ignore the front portion of the array
            # and keep forming subarrays in the later parts of the array
    return num_subarrays
    
