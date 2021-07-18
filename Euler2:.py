def febonacci_4m(n):
    first, second = 1, 2
    collector = [1, 2]
    while second < n:
        first, second = second, first + second
        collector.append(second)
    return collector

def sum_even(lst):
    return sum([i for i in lst if i%2 == 0])

lst = febonacci_4m(4000000)
print(sum_even(lst))