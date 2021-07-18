def multiples_35(n):
    i = 3
    sum1 = 0
    while i < n:
        if (i % 3 == 0 or i % 5 == 0):
            sum1 += i
        i += 1
    return sum1

print(multiples_35(1000))
