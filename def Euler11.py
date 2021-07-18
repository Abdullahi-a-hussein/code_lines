from math import ceil
def Eulera11(n):
    req = 0
    for i in range(1, n + 1):
        req += i
    return req

def factors(n):
    divisor = []
    for i in range(1, ceil(n/2) + 1):
        if n % i == 0:
            divisor.append(i)
    divisor.append(n)
    return len(divisor)


def Euler11(n):
    req = True
    k = 100
    number = 1
    while req:
        m = Eulera11(k)
        if n < factors(m):
            req = False
            number = m
        k += 1
    return number
        


print(Euler11(500))
# print(factors(28))
