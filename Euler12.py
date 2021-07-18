import math, timeit
def triangle_numbers(n):
    #returns a list of triangle numbers up to nth triangle number
    sums = 0
    numbers = []
    for i in range(1, n + 1):
        sums += i
        numbers.append(sums)
    return numbers
def number_of_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if (n/i == i):
                count += 1
            else:
                count += 2

    return count 

def max_divisors(lst):
    target = [1,1]
    for item in lst:
        k = number_of_divisors(item)
        if k > target[0]:
            target[0], target[1]= k, item
            if k > 500:
                break
    return target
start = timeit.default_timer()
lst = triangle_numbers(50000)
print(max_divisors(lst))
stop = timeit.default_timer()
print(stop - start)
