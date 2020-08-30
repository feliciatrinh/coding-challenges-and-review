"""
Input: square board N x N describing Aladdin's and Jafar's pawns
Output: maximum number of pawns owned by Aladdin that Jafar can beat in his turn

Jafar's pawn is described by the 'O' character
Aladdin's pawn is described by the 'X' character
Empty fields are filled with '.'

Board is described from top to bottom and from left to right.

Assume N is integer within [1, 30]
Board contains exactly one pawn owned by Jafar

In checkers, you can defeat your opponents pawn by leaping over their pawn in the up-right or up-left diagonal
directions only if the target square is free. You can defeat multiple pawns, one after another, as long as your target
squares are free.

Example
Input:
B[0] = "..X..."
B[1] = "......"
B[2] = "....X."
B[3] = ".X...."
B[4] = "..X.X."
B[5] = "...O.."
Output: 2
Explanation: Jafar can go top-right and then top-left to end up in B[1][3]

Input:
B[0] = "X....."
B[1] = ".X...."
B[2] = "..O..."
B[3] = "....X."
B[4] = "......"
Output: 0

Ideas
- is this similar to the 'how many paths are there in a grid' problem? in that I need to solve it recursively?
- dfs?
- jumps from B[5][3] tp B[3][5] to B[1][5]
    - first index can only decrease by 2, second index can increase or decrease by 2 from any spot
    - keep track of current position
    - if next position (2 up and 2 to either the left or right) is a '.' and position 1 up and 1 to either the left or
      right is an 'X', then increase the count

Dynamic programming
- Runtime: O(n^2), Space complexity: O(n^2)

- Subproblem: B[i][j] is the number of pawns jafar can own at the end of his turn after landing in position i, j

- Base case: initialize all to zero?

- Recurrence relation:
    B[i][j] = max { B[i + 2][j - 2] + 1 if B[i + 1][j - 1] == "X", B[i + 2][j + 2] + 1 if B[i + 1][j + 1] == "X"}
    if B[i][j] == "." and i + 2, j - 2, j + 2 are valid

- you'd need to check for "O" at every iteration as well?
    - you check if B[i + 2][j - 2] or B[i + 2][j + 2] == "O" every time you try to calculate B[i][j]
    - after checking, you'd change B[i][j] to "O" if it's a free spot that gives you a point so the next iteration
      works?

Final answer: keep track of the running max?
"""


def checkers_game(B):
    """
    Recursive Solution
    Runtime: exponential, Space complexity? recursion stack?
    """
    def get_count(player, direction):
        """
        :param player: jafar's initial position
        :param direction: -1 indicates going left, 1 indicates going right
        :return: number of opponent pawns the player can own
        """
        i, j = player
        target_i = i - 2
        target_j = j + direction * 2
        if 0 <= target_i <= n - 1 and 0 <= target_j <= n - 1:
            if B[i - 1][j + direction] == "X" and B[target_i][target_j] == ".":
                return get_count((target_i, target_j), -1) + get_count((target_i, target_j), 1) + 1
        return 0

    n = len(B)
    # determine Jafar's position
    jafar = (-1, -1)
    for i in range(n):
        for j in range(n):
            if B[i][j] == "O":
                jafar = (i, j)
                break

    return max(get_count(jafar, -1), get_count(jafar, 1))


def checkers_game_dp(B):
    """
    Dynamic Programming solution
    Runtime: O(n^2), Space complexity: O(n^2)
    """
    def get_count(player, direction, grid, counts):
        """
        :param player: jafar's final position
        :param direction: -1 indicates coming from the left, 1 indicates coming from the right
        :return: number of opponent pawns the player can own by the time player reaches final position
        """
        i, j = player
        prev_i = i + 2
        prev_j = j + direction * 2
        if 0 <= prev_i <= n - 1 and 0 <= prev_j <= n - 1:
            if board[i + 1][j + direction] == "X" and board[prev_i][prev_j] == "O":
                board[i][j] = "O"
                return counts[prev_i][prev_j] + 1
        return 0

    # convert B into a list of lists where each element is a list representing that row of the checker board
    n = len(B)
    board = [list(B[i]) for i in range(n)]

    P = []
    for _ in range(n):
        P.append([0 for _ in range(n)])

    max_count = 0
    # any final position with non-zero points cannot be in the last two rows so i starts at (n - 1) - 2
    for i in range(n - 3, -1, -1):
        for j in range(n):
            if board[i][j] == ".":
                P[i][j] = max(get_count((i, j), -1, board, P), get_count((i, j), 1, board, P))
                max_count = max(max_count, P[i][j])
    return max_count


B0 = "..X..."
B1 = "......"
B2 = "....X."
B3 = ".X...."
B4 = "..X.X."
B5 = "...O.."

B = [B0, B1, B2, B3, B4, B5]
assert checkers_game(B) == 2
assert checkers_game_dp(B) == 2

B0 = "X....."
B1 = ".X...."
B2 = "..O..."
B3 = "....X."
B4 = "......"
B = [B0, B1, B2, B3, B4]
assert checkers_game(B) == 0
assert checkers_game_dp(B) == 0

B0 = "X....."
B1 = ".X.X.."
B2 = "..O..."
B3 = "....X."
B4 = "......"
B = [B0, B1, B2, B3, B4]
assert checkers_game(B) == 1
assert checkers_game_dp(B) == 1
