'''Tabulated version of fibonacci.'''
import pyinputplus as pyip

def fib(n):
    # Initialise base values.
    table = [None] * (n + 1)
    table[0] = 0
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]


def main():
    n = pyip.inputInt("Enter an integer: ")

    print(f"Fib(n) is {fib(n)}")


if __name__ == '__main__':
    main()