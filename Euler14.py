

def collatz(n):
    # return collatz chain with starting number n
    container = [n]
    while n > 1:
        n = n//2 if n%2 == 0 else 3*n+1
        container.append(n)
    return len(container)

print(collatz(13))

def largest_collatz(n):
    # returns the number less than n with the longest chain of collatz sequence 
    number = 1
    chain_lenght = 1
    for i in range(1, n):
        chain = collatz(i)
        if chain > chain_lenght:
            chain_lenght = chain
            number = i
    return number

print(largest_collatz(1000000))
print((2**1000))