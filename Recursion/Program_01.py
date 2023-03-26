# This is a simple python program to demonstrate recursion.
# It prints all numbers from 1 to 'n' using recursion.
# If the number 'n' is less than 1, the program just gets executed without any errors.

def recursiveMethod(n):
    if n < 1:
        return
    else:
        recursiveMethod(n-1)
        print(n)


recursiveMethod(5)

"""
The output is as follows:
1
2
3
4
5
"""
