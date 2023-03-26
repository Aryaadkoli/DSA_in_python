# Calculate fibonacci number in the 'n'th position using recursion.
# It goeas as follows: 0 1 1 2 3 5 8 13 21 34 ....
# 0th element is 0, 1st element is 1,..., 7th element is 13 and so on.

def fibonacci(n):
    assert n >= 0 and int(n) == n, "Fibonacci number cannot be determined for a negative number or non integer number"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))

"""
The output is as follows:
3
"""
