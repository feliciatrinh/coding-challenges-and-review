#  Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. First and last cloud are always 0. c is an array of binary integers. 

def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c)-1: 
        if i+2 < len(c) and c[i+2] == 0: 
            i += 2
        else: 
            i += 1
        jumps += 1
    return jumps
