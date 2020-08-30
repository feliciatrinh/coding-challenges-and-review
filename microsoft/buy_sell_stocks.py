"""
Given a timeline for a stock (A chronologically ordered list of day objects containing the highest
and lowest price for the stock on that day) find the date to buy and the date to sell that would result
in the highest profit.

Assume I cannot buy and sell on the same day and that I have to make one buy and one sell.
Assume timeline can't be empty

Maximize sell_i - buy_j for i > j where i and j are days

TODO: optimize?
"""


class Day:
    def __init__(self, day, buy, sell):
        self.day = day
        self.buy = buy
        self.sell = sell


def buy_sell_stocks_naive(timeline):
    """
    Runtime: O(n^2)
    """
    profit = -timeline[0].buy
    date_buy = None
    date_sell = None
    for i in range(1, len(timeline)):
        sell_day = timeline[i]
        for j in range(i):
            buy_day = timeline[j]
            new_prof = sell_day.sell - buy_day.buy
            if new_prof > profit:
                profit = new_prof
                date_buy = buy_day.day
                date_sell = sell_day.day
    return date_buy, date_sell


day1 = Day(1, 7, 7)
day2 = Day(2, 1, 1)
day3 = Day(3, 5, 5)
day4 = Day(4, 3, 3)
day5 = Day(5, 6, 6)
day6 = Day(6, 4, 4)

assert buy_sell_stocks_naive([day1, day2, day3, day4, day5, day6]) == (2, 5)
