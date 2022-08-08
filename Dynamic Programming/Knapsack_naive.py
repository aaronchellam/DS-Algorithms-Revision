"""
A naive recursive implementation of Knapsack Problem
"""


def knapSack(W, weights, values, n):
    """
    Returns the maximum value that can be put in a knapsack of capacity W

    :param W: Capacity of sack
    :param weights: List of weights for each item
    :param values: List of values for each item
    :param n: Number of items
    """

    # Base Case
    if n == 0 or W == 0:
        return 0

    # If the weight of the nth item is more than the capacity W, then this item cannot be included in the final
    # optimal solution.
    if weights[n - 1] > W:
        return knapSack(W, weights, values, n-1)


    # Return the maximum of two cases:
    # (1) nth item included
    # (2) nth item not included

    else:
        case1 = values[n-1] + knapSack(W - weights[n-1], weights, values, n-1)
        case2 = knapSack(W, weights, values, n-1)

        return max(case1, case2)


# Driver Code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
