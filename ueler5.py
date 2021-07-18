def is_prime(n):
    if n == 2:
        return True
    first = 2
    while first < n:
        if n % first == 0:
            return False
        first += 1
    return True

def euler5(n):
    """Return the product of all prime numbers that are less than or equal to n"""
    i = 2
    product = 1
    while i <= n:
        if is_prime(i):
            product *= i
        i += 1
    return product

def lcm(n):
    """Return the lcm of the list of numbers"""
    numbers = [x for x in range(2, n + 1)]

    product = 1
    divider = 2
    while divider < max(numbers):
        numbers1 = numbers[:]
        mul = False
        for j in range(len(numbers)):
            if numbers1[j] % divider == 0:
                numbers1[j] = numbers1[j]/divider
                mul = True
        if mul:
            product *= divider
        if mul is False:
            divider += 1
        print(numbers1)
        numbers = numbers1
    for k in numbers:
        product *= k
    return product

print(lcm(10))
print(lcm(20))

            

