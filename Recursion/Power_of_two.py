# Python program to  find and print powers of 2 upto any particular number 'n'.
# Example: 2^5 = 32.

def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2


print(powerOfTwo(5))

"""
The output is:
32
"""
