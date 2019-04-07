# sort a list by using mergesort; split the list in halves and sort each half then merge together
# recursive solution

def mergesort(lst): 
    if len(lst) <= 1: 
        return lst
    middle = len(lst)//2
    return merge(mergesort(lst[:middle]), mergesort(lst[middle:]))
    
def merge(lst1, lst2):
    if len(lst1) == 0: 
        return lst2
    elif len(lst2) == 0: 
        return lst1
    elif lst1[0] < lst2[0]: 
        return [lst1[0]] + merge(lst1[1:], lst2)
    return [lst2[0]] + merge(lst1, lst2[1:])
