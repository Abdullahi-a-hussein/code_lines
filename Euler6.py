def Euler6(n):
    """Return the difference between the sum of squares and square of the sum of the first n numbers"""
    sqsum = 0
    sumsq = 0
    for i in range(1, n + 1):
        sqsum += i**2
        sumsq += i
    return (sumsq**2 - sqsum)

print(Euler6(100))