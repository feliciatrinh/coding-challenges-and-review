"""
Source: Leetcode
Input: array for which the i-th element is the price of a given stock on day i
Output: maximum profit given you can complete at most k transactions

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Runtime: O(nk)
Space complexity: O(n) if memory efficient, O(nk) if not

Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Subproblem:
P(i, j) is the maximum profit you can have at the end of the i-th day with j transactions remaining

We keep decrement the number of transactions remaining whenever we buy.

Possible actions on day i:
Sell the stock: P(i - 1, j) + prices[i]
Buy the stock: P(i - 1, j - 1, 0) - prices[i] when j > 0

Recurrence relation:
P(i, j) =

Final answer:
P(n - 1, k)

if 2 * k >= n, you can have max or more transactions than would be possible with n days. So you can solve the problem
using the basic solution from the non-dynamic programming version of the problem.
"""


def basic_solution(prices):
    """
    Runtime: O(n)
    """
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


def buy_sell_stocks(k, prices):
    """
    Runtime: O(nk), Space complexity: O(nk)
    """
    if not prices or k <= 0:
        return 0

    length = len(prices)

    if 2 * k >= length:
        return basic_solution(prices)

    P = []
    for _ in range(length):
        P.append([0 for _ in range(k + 1)])

    for j in range(1, k + 1):
        # temp_max is initially the money spent on buying the first stock b/c you can't sell w/o having bought one first
        temp_max = - prices[0]
        for i in range(1, length):
            # prices[i] + temp_max is profit if we sell the ith stock
            # sell the stock if the profit is higher than the last
            P[i][j] = max(P[i - 1][j], prices[i] + temp_max)
            # P[i - 1][j - 1] - prices[i] is profit if we buy the ith stock, buying counts towards the transaction count
            # temp_max is max {profit using at most the first i - 1 prices and doing at most j - 1 transactions,
            #                  profit after buying stock i}
            # buy the stock if the cost is lower than the last
            temp_max = max(temp_max, P[i - 1][j - 1] - prices[i])
    return P[length - 1][k]


def buy_sell_stocks_alt(k, prices):
    """
    Runtime: O(nk), Space complexity: O(n)
    """
    if not prices or k <= 0:
        return 0

    length = len(prices)

    if 2 * k >= length:
        return basic_solution(prices)

    # TODO: fill in


assert buy_sell_stocks(12, [7, 1, 5, 3, 6, 4]) == 7
assert buy_sell_stocks(2, [2, 4, 1]) == 2
assert buy_sell_stocks(2, [3, 2, 6, 5, 0, 3]) == 7
