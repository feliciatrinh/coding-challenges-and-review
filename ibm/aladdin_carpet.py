"""
Source: Leetcode
See related 134. Gas Station
Input: 2 integer arrays magic and distance
Output: The lowest index Aladdin can start his journey and visit all of the places in a circular path in order,
        or -1 if no solution

Example
Input: magic = [3, 2, 5, 4], distance = [2, 3, 4, 2]
Output: 0

Ideas
- solution is unique if it exists
- For the first example, we do these calculations
magic[0] - dist[0] + magic[1] = 3
3 - dist[1] + magic[2] = 5
5 - dist[2] + magic[3] = 5
5 - dist[3] = 3 >= 0 so we can make the round trip starting from index 0

If we put this all together, it's just checking this at the end
magic[0] - dist[0] + magic[1] - dist[1] + magic[2] - dist[2] + magic[3] - dist[3] >= 0

Let m be an array containing the amount of magic you have left over after leaving stop i.
m[0] = magic[0] - dist[0] and we need magic[0] - dist[0] >= 0 to be true
m[1] = m[0] + magic[1] - dist[1]
m[2] = m[1] + magic[2] - dist[2]

at each i, if m[i] - dist[i] < 0 then you can't go onto the next step. We can then just increment the start point
and keep checking each i

we only use m[i - 1] at each i, so we can replace the m array with something like a remainder variable
Then, it'd be remainder = magic[0] - dist[0]

We always start from 0, so if 0 doesn't work as a starting point, then 1, 2, or some index greater than 0 has to work
- if 1 doesn't end up working then 2 or some higher index has to work and so on
- which is why it works to set start = i + 1 when you get that remainder < 0
"""


def aladdin_carpet(magic, distance):
    """
    Runtime: O(N), Space: O(1)
    """
    start = 0
    remainder = 0
    # sum of magic[i] - distance[i] for all i
    final = 0
    for i in range(len(magic)):
        remainder += magic[i] - distance[i]
        # Aladdin can't make it to the next stop
        if remainder < 0:
            final += remainder
            remainder = 0
            start = i + 1
    if remainder + final < 0:
        return -1
    return start


def aladdin_carpet_alt(magic, distance):
    """
    Runtime: O(N), Space: O(1)
    """
    # sum of magic[i] - distance[i] for all i
    if sum(magic) - sum(distance) < 0:
        return -1

    start = 0
    remainder = 0
    for i in range(len(magic)):
        # Aladdin can't make it to the next stop
        remainder += magic[i] - distance[i]
        if remainder < 0:
            remainder = 0
            start = i + 1
    return start


def aladdin_carpet_bad(magic, distance):
    """
    First attempt
    """
    start = 0
    num_places = len(magic)
    while visited < num_places and start < num_places:
        # magic that Aladdin has after arriving at each place
        m = magic[:]
        for i in range(start + 1, start + num_places):
            index = i % num_places
            print(index)
            visited += 1
            # if Aladdin cannot reach the next stop
            if m[index - 1] - distance[index - 1] < 0:
                break
            else:
                m[index] = m[index - 1] - distance[index - 1] + magic[index]

        if m[start - 1] - distance[start - 1] >= 0 and visited == num_places:
            return start
        start += 1
        visited = 1
    return -1


assert aladdin_carpet([3, 2, 5, 4], [2, 3, 4, 2]) == 0
assert aladdin_carpet([2, 4, 5, 2], [4, 3, 1, 3]) == 1

assert aladdin_carpet_alt([3, 2, 5, 4], [2, 3, 4, 2]) == 0
assert aladdin_carpet_alt([2, 4, 5, 2], [4, 3, 1, 3]) == 1
