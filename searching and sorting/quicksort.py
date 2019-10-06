# quicksort where the first element of the input list is the pivot

def quicksort(lst): 
    if len(lst) == 1: 
        return lst
    pivot = lst[0]
    less = [item for item in lst[1:] if item < pivot]
    greater = [item for item in lst[1:] if item > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
