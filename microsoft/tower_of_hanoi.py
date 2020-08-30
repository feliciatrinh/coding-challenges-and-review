"""
Source: python advanced course topics
Input: 3 rods, n different sized disks in order of smallest to largest from top to bottom starting on rod 1
Output: minimum number of moves required to move the stack from one row to another
- moves are allowed only if you place a smaller disk on top of a larger disk
- move one disk at a time, can only move the top disk of any stack

Runtime: O()
- minimal number of moves is 2^n - 1

- 3 rods acting as start, other, finish
- if there's only one disk, move the disk from start to finish
- for more than one disk, recursively move top n - 1 disks from source to other
    - this will create another tower of hanoi problem that can be solved in the same manner
- then move the last disk to finish rod
- then recursively move n - 1 disks from other to finish
"""


def tower_of_hanoi(n):
    """
    :param n: number of disks
    :return: minimal number of moves to move disks from one rod to another
    """
    if n > 0:
        return tower_of_hanoi(n - 1) + 1 + tower_of_hanoi(n - 1)
    return 0


def tower_of_hanoi_alt(n, start, other, finish):
    """
    start, other, and finish are stacks
    """
    if n > 0:
        tower_of_hanoi_alt(n - 1, start, finish, other)
        if start:
            finish.append(start.pop())
        tower_of_hanoi_alt(n - 1, other, start, finish)


assert tower_of_hanoi(4) == 15

start = [4, 3, 2, 1]
other = []
finish = []
tower_of_hanoi_alt(4, start, other, finish)
assert finish == [4, 3, 2, 1]
