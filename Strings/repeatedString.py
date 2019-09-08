# return an integer representing the number of occurrences of a in the prefix of length n in the infinitely repeating string.
def repeatedString(s, n):
    fullRepeats = n // len(s)
    partial = n % len(s)
    return s.count("a") * fullRepeats + s[:partial].count("a")
