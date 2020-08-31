"""
Input: 4 arrays, each containing the price per unit for that particular item, and a budget
Output: number of ways the shopper can purchase all 4 items

Example
Input: jeans = [2, 3], shoes = [4], skirts = [2, 3], tops = [1, 2], budget = 10
Output: 4
combos that add up to 10 dollars or less are (2, 4, 2, 2), (2, 4, 2, 1), (3, 4, 2, 1), (2, 4, 3, 1)

1 <= a, b, c, d, <= 10^3
1 <= budget <= 10^9
1 <= price of each item <= 10^9

Ideas
- if sum of all minimum elements from each array is > budget then you can't afford an outfit
- if one of the items has only one option, then you can reduce the budget by that amount and recursively solve for
  the rest of the items if you choose not to have that min check at the beginning because min on an empty array errors
- brute force: try all combinations possible, sum up the total and see if it's within budget
- backtracking? exponential runtime

- should i sort each price array first? -> wasn't needed
- memoization to avoid recomputing?
- I need someway to store past results
- starting with jeans, the number of combos with price jeans[0], jeans[1],..., jeans[n] is each 1
    - then you move onto shoes. the number of combos with price jeans[0] + shoes[0] gets incremented by the num of
      combos with jeans[0]. same with jeans[0] + shoes[1]. same with the number of combos with price jeans[0] + shoes[1]
    - do the same for all items
- I can keep a list or dictionary where the key is the price of the current combo
"""


def shoppers_delight(jeans, shoes, skirts, tops, budget):
    """
    First attempt, Backtracking
    Runtime: exponential?, Space: O(N)?
    """
    if min(jeans) + min(shoes) + min(skirts) + min(tops) > budget:
        return 0

    def shop(group, cost):
        if cost > budget:
            return 0

        # we finished an outfit combination that's within budget
        if group == len(groups) and cost <= budget:
            return 1

        options = 0
        for price in groups[group]:
            options += shop(group + 1, cost + price)
        return options

    groups = [jeans, shoes, skirts, tops]
    return shop(0, 0)


def shoppers_delight_alt(jeans, shoes, skirts, tops, budget):
    """
    Runtime: O(N^3) where N is the average length of the clothing arrays, Space: O(N)? Space should be larger?
    """
    if min(jeans) + min(shoes) + min(skirts) + min(tops) > budget:
        return 0

    # cost_to_counts maps total cost to the number of combos with that total cost
    cost_to_counts = {price: 1 for price in jeans}
    items = [shoes, skirts, tops]
    for item in items:
        # temp temporarily maps total cost to the number of combos with that total cost as we build our new combinations
        temp = dict()
        for cost, count in cost_to_counts.items():
            # calculate if we can afford to add the next item to each of our current combos
            for next_item_price in item:
                total_cost = cost + next_item_price
                if total_cost <= budget:
                    if total_cost in temp:
                        temp[total_cost] += count
                    else:
                        temp[total_cost] = count
        # discard our old combos and keep the new ones
        cost_to_counts = temp
    return sum(cost_to_counts.values())


def test(function):
    assert function([2, 3], [4], [2, 3], [1, 2], 10) == 4
    assert function([2, 3], [4], [2], [1, 2, 3], 10) == 3
    assert function([4], [3, 4, 1], [3, 2], [4], 12) == 2
    assert function([1], [4], [3], [1], 3) == 0


functions = [shoppers_delight_alt]
for func in functions:
    test(func)
