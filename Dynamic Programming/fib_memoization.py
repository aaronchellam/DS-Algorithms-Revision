""" Memoized version of Fibonacci."""
import pyinputplus as pyip

def fib(n, lookup_table):
    # Base case.
    if n <= 1:
        lookup_table[n] = n

    # If the value is not stored in the table, calculate it and store in table.
    if lookup_table[n] is None:
        lookup_table[n] = fib(n-1, lookup_table) + fib(n-2, lookup_table)

    # Return value corresponding to fib(n) using table - every computed value is stored.
    return lookup_table[n]


def main():
    n = pyip.inputInt("Enter an integer: ")

    # Initialise lookup table with null values.
    lookup = [None] * (n+1)

    print(f"Fib(n) is {fib(n, lookup)}")


if __name__ == '__main__':
    main()