"""
Input: string s of length M containing the seats that are already reserved separated by exactly 1 space
Output: maximum number of four-person families you can fit

- A four-person family occupies four seats in one row that are next to each other
- a family can be split across an aisle but exactly 2 people have to sit on each side of the aisle

Seats are like
   A  B  C    D  E  F  G    H  J  K
1
2
.
.
.
N

So there are 10 aisles and N rows

Example
Input: N = 2, s = "1A 2F 1C"
Output: 2


Ideas
- Keep a 2D array 10 x N called r where r[i][j] is the seat at row i, aisle j
- iterate through the string s and fill in the occupied seats with False
- at the end, iterate through r to calculate how many families you can fit at most
- all(r[i][1:9])  means you can fit 2 fams, if not this then
- all(r[i][1:5]) or all(r[i][5:9]) or all(r[i][3:7]) means you can fit one fam
Runtime: O(M) + O(10 * N) -> O(M + N)
Space: O(10N) + O(10) -> O(N)

- calculate the max num of fams possible
- iterate through s and subtract from the num of fams possible accordingly?
- this way, when you get a reserved seat for a row that already cannot fit 4 people, you can just continue
    - you'd have to keep a set of rows that already cannot fit 4 people?
- you'd keep a reserved array r that's 3 X N for the 3 different sections that can possibly fit 4 people?
- or just map all the rows to the reserved cols, then iterate through these and subtract from num_fams based on which
  section the col corresponds to
    - col in (2, 3, 4, 5) is section 1
    - col in (4, 5, 6, 7) is section 2
    - col in (6, 7, 8, 9) is section 3
    - if col is in section 1 then it's possible to have 1 fam fit in either section 2 or 3
    - if col is in section 2 then it's impossible to fit any fam
    - if col is in section 3 then it's the same case as section 1
    - which is why we do max_num_fams += count - 2  b/c each row could fit a maximum number of 2 fams to begin with
Runtime: O(M), Space: O(M)

- i can also get a list out of the string by doing s.split(' ') but  I'm trying not to use any built-in functions
- can do the same as solution 2 except sort in-place first to get runtime O(MlogM) and space O(1)
"""


def plane_seat(N, s):
    """
    Does not meet time requirements.
    Runtime: O(N + M), Space: O(N)
    """
    def row_col(seat):
        """
        Returns the corresponding row and column for the given seat number.
        Remember that the row number can be multiple digits, but the aisle number will always be a single digit.
        """
        aisle = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "J": 8, "K": 9}
        return int(seat[:len(seat) - 1]) - 1, aisle[seat[-1]]

    r = [[True for _ in range(10)] for _ in range(N)]
    curr_seat = ""
    for k in range(len(s) + 1):
        if k == len(s) or s[k] == " ":
            i, j = row_col(curr_seat)
            # if seat (i, j) is reserved then r[i][j] is False
            r[i][j] = False
            curr_seat = ""
        else:
            curr_seat += s[k]

    num_fams = 0
    for i in range(N):
        sections = 0
        if all(r[i][1:9]):
            num_fams += 2
        elif all(r[i][1:5]) or all(r[i][3:7]) or all(r[i][5:9]):
            num_fams += 1
    return num_fams


def plane_seat_alt(N, s):
    """
    Runtime: O(M), Space: O(M)
    """
    def row_col(seat):
        """
        Returns the corresponding row and col for the given seat number.
        Remember that the row number can be multiple digits, but the aisle letter will always be a single character.
        """
        aisle = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "J": 9, "K": 10}
        row = int(seat[:len(seat) - 1])
        col = aisle[seat[-1]]
        return row, col

    reserved = dict()
    curr_seat = ""
    for k in range(len(s) + 1):
        if k == len(s) or s[k] == " ":
            i, j = row_col(curr_seat)
            if i not in reserved:
                reserved[i] = {j}
            else:
                reserved[i].add(j)
            curr_seat = ""
        else:
            curr_seat += s[k]

    num_fams = 2 * N
    for _, cols in reserved.items():
        sections = 0
        if not any(col in cols for col in (2, 3, 4, 5)):
            sections += 1
        if not any(col in cols for col in (6, 7, 8, 9)):
            sections += 1
        # check if sections == 0 to avoid double counting where the sections overlap
        if sections == 0 and not any(col in cols for col in (4, 5, 6, 7)):
            sections += 1
        num_fams += sections - 2
    return num_fams


def plane_seat_leetcode(n, reserved_seats):
    """
    Source: Leetcode
    Runtime: O(M), Space: O(M)
    reserved_seats is a list of lists e.g. [[4, 3], [1, 2]]
    """
    reserved = dict()
    for seat in reserved_seats:
        row, col = seat
        if row not in reserved:
            reserved[row] = {col}
        else:
            reserved[row].add(col)

    groups = 2 * n
    for _, cols in reserved.items():
        sections = 0
        if not any(col in cols for col in (2, 3, 4, 5)):
            sections += 1
        if not any(col in cols for col in (6, 7, 8, 9)):
            sections += 1
        # check if sections == 0 to avoid double counting where the sections overlap
        if sections == 0 and not any(col in cols for col in (4, 5, 6, 7)):
            sections += 1
        groups += sections - 2
    return groups


assert plane_seat(2, "1A 2F 1C") == 2
assert plane_seat(3, "1B 1C 2F 3K 1H 3A") == 4

assert plane_seat_alt(2, "1A 2F 1C") == 2
assert plane_seat_alt(3, "1B 1C 2F 3K 1H 3A") == 4

assert plane_seat_leetcode(4, [[4, 3], [1, 4], [4, 6], [1, 7]]) == 4
assert plane_seat_leetcode(3, [[1, 2], [1, 3], [2, 6], [3, 10], [1, 8], [3, 1]]) == 4
