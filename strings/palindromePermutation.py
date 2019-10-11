from collections import Counter
import re

def pali(str): 
    if len(str) == 1: 
        return True
    str = str.lower()
    str = re.sub(r"\s", "", str)
    letters = Counter()
    for char in str: 
        letters[char] += 1
    odd_only = 0
    for char in str: 
        if letters[char] % 2 != 0: 
            odd_only += 1
    if odd_only > 1: 
        return False
    return True
 
 print(pali("a") == True)
 print(pali("racecar") == True)
 print(pali("abd c") == False)
 
