"""
Input: a list representing a line configuration
Output: print integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is
        not possible.

Print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not
possible.
One person can at most bribe two people, can only bribe the person directly in front of them
"""


def minimum_bribes(q):
    jumps = 0
    q = [val - 1 for val in q]
    for i, original in enumerate(q): 
        # i is the current position aka index
        # original is the value aka the original position
        if (original - i) > 2: 
            print("Too chaotic")
            return
        # max(original-1, 0) to avoid negative indexing
        # subtract 1 b/c people can at most be 1 space ahead of you if you've received one bribe
        for j in range(max(original - 1, 0), i): 
            if original < q[j]: 
                jumps += 1
    print(jumps)
