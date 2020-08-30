"""
Source: Leetcode
Input: array of meeting time intervals consisting of integer start and end times [[s1, e1], [s2, e2], ...]
Output: minimum number of conference rooms required

Ideas
- min num of conference rooms is maximum number of meetings that overlap at any one time?
- need to sort intervals by start time and keep track of the earliest ending time
    - sort all intervals by start time and throw all ending times into a separate min-heap
    - for each interval, if the start time is after or at the ending time of the meeting at the top of the heap, then
      you do not need to add a room (b/c you can re-use the room the top of the heap is using) and you can remove the
      top of the heap
"""


def meeting_rooms(intervals):
    """
    Runtime: O(NlogN), Space: O(N)
    """
    import heapq

    intervals.sort(key=lambda x: x[0])
    ends_heap = []
    rooms = 0
    for interval in intervals:
        start, end = interval
        if not ends_heap:
            rooms += 1
        elif start >= ends_heap[0]:
            heapq.heappop(ends_heap)
        else:
            rooms += 1
        heapq.heappush(ends_heap, end)
    return rooms


def meeting_rooms_alt(intervals):
    """
    Simply return the length of the heap at the end.
    Runtime: O(NlogN), Space: O(N)
    """
    import heapq

    intervals.sort(key=lambda x: x[0])
    ends_heap = []
    for interval in intervals:
        start, end = interval
        if ends_heap and ends_heap[0] <= start:
            heapq.heappop(ends_heap)
        heapq.heappush(ends_heap, end)
    return len(ends_heap)


assert meeting_rooms([[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]]) == 2
assert meeting_rooms([[5, 20], [1, 7], [2, 10]]) == 3
assert meeting_rooms([]) == 0
assert meeting_rooms([[14, 17], [11, 13], [10, 16]]) == 2
assert meeting_rooms([[14, 17]]) == 1

assert meeting_rooms_alt([[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]]) == 2
assert meeting_rooms_alt([[5, 20], [1, 7], [2, 10]]) == 3
assert meeting_rooms_alt([[14, 17], [11, 13], [10, 16]]) == 2
assert meeting_rooms_alt([[14, 17]]) == 1
