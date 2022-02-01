##https://projecteuler.net/problem=3

n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i;
    i = i + 1
#continues going up until finds the highest divisible 
#number

print(n)
