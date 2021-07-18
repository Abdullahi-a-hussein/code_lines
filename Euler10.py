from math import floor, sqrt
def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i <= floor(sqrt(n)):
            if n % i == 0:
                return False
            i += 2
        return True

def Euler10(n):
    i = 3
    count = 2
    while i < n:
        if is_prime(i):
            count += i
        i += 2
    return count

print(Euler10(2000000))