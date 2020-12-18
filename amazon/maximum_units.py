"""
Input: num: integer representing number of products,  boxes: list of integers representing number of available boxes
       for products, unit_size: integer representing size of units_per_box, units_per_box: list of integers representing
       number of units packed in each box, truck_size: integer representing number of boxes truck can carry
Output: maximum number of units of any mix of products that can be shipped

Example
Input: num=3, boxes=[1, 2, 3], unit_size=3, units_per_box=[3, 2, 1], truck_size=3
Output: 7 because the possible boxes you can add to the truck have units of [3, 2, 2, 1, 1, 1] and 3 + 2 + 2 = 7

Ideas
- keep a dictionary of unitPerBox to number of boxes containing this many units
    - keep track of the maximum unitPerBox number
    - start with the maximum unitPerBox, query for the maximum num of boxes with this many units that you can pack into
      the truck
    - decrement the maximum unitPerBox number and continue querying and updating the dictionary until you get down to 0
      unitPerBox or the truck is full
    - can use collections library to make it cleaner
    Runtime: O(max{unit_size, max(units_per_box)})? or is it max(units_per_box) * max(box[i])?
             or is it unit_size * max(box[i])
    Space: O(N) where N is unit_size

- use a max heap instead to keep track of the largest number of units you can add to the truck
"""


def maximum_units(num, boxes, unit_size, units_per_box, truck_size):
    """
    First attempt
    Runtime: O(N*M)?
    Space: O(N) where N is unit_size
    """
    units_to_num_boxes = dict()
    curr_max_units = 0
    num_units_in_truck = 0
    num_boxes_in_truck = 0
    for i in range(unit_size):
        if units_per_box[i] in units_to_num_boxes:
            units_to_num_boxes[units_per_box[i]] += boxes[i]
        else:
            units_to_num_boxes[units_per_box[i]] = boxes[i]
        curr_max_units = max(curr_max_units, units_per_box[i])

    while curr_max_units > 0 and num_boxes_in_truck < truck_size:
        if curr_max_units in units_to_num_boxes:
            num_boxes = units_to_num_boxes[curr_max_units]
            for j in range(num_boxes):
                if num_boxes_in_truck + 1 <= truck_size:
                    num_units_in_truck += curr_max_units
                    num_boxes_in_truck += 1
        curr_max_units -= 1

    return num_units_in_truck


def maximum_units_heap(num, boxes, unit_size, units_per_box, truck_size):
    """
    Keep track of the current maximum units you can add to the truck using a max heap instead.
    Greedily add the top of the max heap until the truck is full.
    Runtime: O(NMlog(NM)), Space: O(N * M) where N is unit_size and M is max{boxes[i]}?
    """
    import heapq

    units_max_heap = []
    for i in range(unit_size):
        for j in range(boxes[i]):
            units_max_heap.append(-units_per_box[i])

    num_units_in_truck = 0
    num_boxes_in_truck = 0
    while num_boxes_in_truck < truck_size and units_max_heap:
        num_units_in_truck += -heapq.heappop(units_max_heap)
        num_boxes_in_truck += 1
    return num_units_in_truck


def maximum_units_heap_alt(num, boxes, unit_size, units_per_box, truck_size):
    """
    Could also just sort units_max_heap and pop and add the back of the array instead of using it like an actual heap.
    Runtime: O(NMlog(NM)), Space: O(N * M) where N is unit_size and M is max{boxes[i]}?
    """
    units = []
    for i in range(unit_size):
        for j in range(boxes[i]):
            units.append(units_per_box[i])
    units.sort()

    num_units_in_truck = 0
    num_boxes_in_truck = 0
    while num_boxes_in_truck < truck_size and units:
        num_units_in_truck += units.pop()
        num_boxes_in_truck += 1
    return num_units_in_truck


def test(function):
    assert function(3, [1, 2, 3], 3, [3, 2, 1], 3) == 7
    assert function(3, [1, 2, 3], 3, [3, 2, 1], 4) == 8
    assert function(3, [2, 5, 3], 3, [3, 2, 1], 50) == 19


functions = [maximum_units, maximum_units_heap, maximum_units_heap_alt]
for func in functions:
    test(func)
