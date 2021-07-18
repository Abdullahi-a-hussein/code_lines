
def Euler3(n):
    """Return the largest prime factor of n"""
    last= 1
    first = 2
    while n > 1:
        if n % first == 0:
            last = first
            n = n/first
        first += 1
    return last
print(Euler3(600851475143))
