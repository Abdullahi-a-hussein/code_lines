from math import ceil, sqrt

def is_prime(n):
    if n == 2:
        return True
    first = 2
    while first <= ceil(sqrt(n)):
        if n % first == 0:
            return False
        first += 1
    return True

def Euler7(n):
    """Return the nth prime number"""
    counter = 0
    current = 1
    i = 2
    while counter < n:
        if is_prime(i):
            current = i
            counter += 1
        i += 1
    return current

print(Euler7(6))
print(Euler7(10001))
