from collections import Counter
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors = Counter()
    for i in range(n):
        colors[ar[i]] += 1
    pairs = 0
    for color in colors: 
        pairs += int(colors[color]/2)
    return pairs
