"""
Calculate the nth fibonacci number iteratively, recursively, tail recursively, etc.
Analyze runtime for each. 
"""


def fib1(n): 
    """
    Simplest recursive algorithm. 
    Runtime theta(2^0.684n), exponential
    """
    if n == 0: 
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)


def fib2(n, k, f0, f1):
    """
    Recursive approach that avoids redundant computations.
    Runtime O(n)
    """
    if n == k:
        return f0
    return fib2(n, k + 1, f1, f0 + f1)


def fib3(n):
    """
    Iterative approach that uses additional space O(n)
    Runtime O(n), linear
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else: 
        a = [0, 1]
        for i in range(2, n + 1):
            a.append(a[i - 1] + a[i - 2])
        return a[n] 


def fib4(n):
    """
    Iterative approach that uses no additional data structures
    Runtime O(n), linear
    """
    if n == 0: 
        return 0
    if n == 1: 
        return 1
    prev = 0
    curr = 1
    for i in range(2, n + 1): 
        temp = curr
        curr = prev + curr
        prev = temp
    return curr


def random_fib(k):
    """
    :param k: integer
    :return: a random fibonacci number less than k

    Runtime: O(logk) assuming calculating the fibonacci numbers is exponential
    if k is invalid, return -1
    """
    from random import choice

    if k <= 0:
        return -1

    if k == 1:
        return 0

    fibs = [0, 1]
    for i in range(2, k):
        next_fib = fibs[i - 2] + fibs[i - 1]
        if next_fib < k:
            fibs.append(next_fib)
        else:
            break
    return choice(fibs)
