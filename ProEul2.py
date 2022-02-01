##https://projecteuler.net/problem=2

a, b, c = 1, 2, 0
sum = 0

#goes through fibonacci until it hits 4 million
while c < 4000000: 
    c = a + b
    a = b
    b = c
    if c % 2 == 0:
        sum += c
        #adds sum of fibonacci if they're even numbers
        
print(sum + 2)
#prints sum + 2 because first run through ignores 2
