"""(Iterative) DP Implementation  of Longest Increasing Subsequence (LIS).
    Solution is O(n^2)
"""


global table


def lis(arr, n):
    """Compute the LIS of arr, ending at index n-1"""

    global table

    # L(k) = 1 + max(L(j)), where 0 <= j < k and arr[k] > arr[j]
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                table[i] = max(table[i], 1 + table[j])





def main():
    # Global table stores the LIS values that have already been computed.
    global table

    # test_arrays
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    # arr = [3, 10, 2, 11]
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 2]

    n = len(arr)

    table = [1] * n

    lis(arr, n)

    # Print
    print(f"The longest increasing subsequence is {max(table)}")


if __name__ == '__main__':
    main()
