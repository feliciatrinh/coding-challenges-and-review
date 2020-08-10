"""
Input: positive integer
Output: score for the integer

Scoring System
+1 for every 7
+3 for each pair of consecutive 5's
+N^2 for a sequence of length N (N >= 1) where each digit is 1 less than the previous digit
    - Example: 9765320 (9 - 765 - 32 - 0) = 1 + 3^2 + 2^2 + 1 = 15 points
+2 if entire number is a multiple of 3
+4 for each even digit (zero counts as even)
"""


def compute_number_score(x):
    def multiple_3(num):
        if num % 3 == 0:
            return 2

    def seven_even(num):
        score = 0
        for digit_str in num:
            digit = int(digit_str)
            if digit == 7:
                score += 1
            if digit % 2 == 0:
                score += 4
        return score

    def fives(num):
        score = 0
        for i in range(len(num) - 1):
            if int(num[i]) == 5 and int(num[i - 1]) == 5:
                score += 3
        return score

    def sequence(num):
        score = 0
        length = 1
        for i in range(1, len(num)):
            if int(num[i]) == int(num[i - 1]) - 1:
                length += 1
            else:
                score += length**2
                length = 1
        score += length**2
        return score

    score = 0
    score += multiple_3(x)

    x = str(x)
    score += seven_even(x)
    score += fives(x)
    score += sequence(x)
    return score


def compute_number_score_alt(x):
    score = 0
    if x % 3 == 0:
        score += 2

    x = str(x)
    length = 1
    for i in range(len(x)):
        curr_digit = int(x[i])
        if curr_digit == 7:
            score += 1
        if curr_digit % 2 == 0:
            score += 4
        if i != len(x) - 1:
            next_digit = int(x[i + 1])
            if curr_digit == 5 and next_digit == 5:
                score += 3
            if curr_digit == next_digit + 1:
                length += 1
            else:
                score += length**2
                length = 1
    score += length**2
    return score


assert compute_number_score(765) == 16
assert compute_number_score_alt(765) == 16
