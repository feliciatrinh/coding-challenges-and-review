"""
Source: hackerrank
"""


def counting_valleys(n, s):
    mounts = 0
    valleys = 0
    num_vals = 0
    for i in range(n): 
        if mounts != 0 and s[i] == "D":
            mounts -= 1
        elif valleys != 0 and s[i] == "U": 
            valleys += 1
            if valleys == 0: 
                num_vals += 1
        elif s[i] == "U": 
            mounts += 1
        else: 
            valleys -= 1
    return num_vals
