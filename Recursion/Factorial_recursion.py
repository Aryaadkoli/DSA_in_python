# Program to find the factorial of a number using recursion.
# If 'n' = 0 or 1, the output will be 1 as 0! = 1 and 1! = 1 too.

def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer only"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
