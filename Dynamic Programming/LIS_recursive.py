"""Recursive implementation of Longest Increasing Subsequence (LIS) problem"""

# Global variable to store the LIS of the input array.
global maximum


def _lis(arr, n):
    """


    :param arr: Input Array
    :param n: Size of input array
    :return: Given an array of size n, returns the size of the LIS.
    """

    # Enable access to global variable.
    global maximum

    # Base Case
    if n == 1:
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1], i.e., the LIS of the local input array
    maxEndingHere = 1

    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] and find max LIS for array ending with arr[n-1].
    """
    for i in range(1, n):
        # _lis(arr, i) is the size of the lis ending at index i-1.
        # The for loop considers the size of the lis for every ending index from 0 to n-2 (array size 1 to n-1)
        res = _lis(arr, i)

        # The check "arr[i-1] < arr[n-1]" is required to guarentee that the subsequence remains increasing.
        # We also check if "res+1 > maxEndingHere" so that maxEndingHere is only updated when a larger increasing
        # subsequence has been found.
        if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1

    # The LIS of the original input array may end either at index n-1 or some smaller index i < n-1.
    # Hence, only update the global maximum variable if maxEndingHere > maximum.
    maximum = max(maximum, maxEndingHere)

    return maxEndingHere


def lis(arr):
    global maximum
    maximum = 1
    n = len(arr)

    # The _lis() function updates the global maximum value when it finds a new LIS.
    _lis(arr, n)
    return maximum


def main():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(f"Length of LIS is {lis(arr)}")


if __name__ == '__main__':
    main()