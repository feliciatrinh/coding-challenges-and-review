# Shift each element d units to the left; 1<=d<=n where n is length of the array a


def rot_left(a, d):
    if d == len(a):
        return a
    return a[d:len(a)] + a[:d]
