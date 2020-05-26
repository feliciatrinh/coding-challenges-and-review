"""
Source: hackerrank
Input: the values of n, k, and b for trips to the store
Output: print which boxes Papyrus must purchase during each trip

Given the values of n, k, and b for trips to the store, determine which boxes Papyrus must purchase during each trip.
- purchases exactly b boxes, have k boxes availble at the store where each box contains k sticks, want n sticks total
- outputs one possible solution
"""


def bonetrousle(n, k, b):
    # First figure out if you have a valid n value, so let's find the range of possible n
    # sum of the first b values from arithmatic sum formula is the minimum n value possible
    min_val = b * (1 + b) // 2
    # sum of the last b values aka (k-b+1) + (k-b+2)+...+k is max n val possible
    max_val = b * (k - b + 1 + k) // 2
    # if n input is outside of possible range, no combos of boxes possible
    if n < min_val or n > max_val: 
        print(-1)
        return

    boxes = range(1, b + 1)
    # Can add the same multiple to each box to get as close to n as possible
    add_all = (n - min_val) // b
    boxes = [box + add_all for box in boxes]
    # Now add the remainder needed to get to n starting from the last element to avoid duplicates
    remainder = int((n - min_val) % b)
    for i in range(remainder): 
        boxes[b - 1 - i] += 1
    # print each box in boxes in one line separated by a space
    print(*boxes)
