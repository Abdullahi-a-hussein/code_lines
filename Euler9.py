def p_triplet(a, b, c):
    return a**2 + b**2 == c**2

def Euler9(n):
    i = 3
    while i < n:
        j = i
        while j < n:
            if p_triplet(i, j, (n - (i +j))):
                return i * j* (n - (i + j))
            j += 1
        i += 1
    return ("nothing")

print(Euler9(1000))