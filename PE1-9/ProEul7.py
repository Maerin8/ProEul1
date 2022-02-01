##https://projecteuler.net/problem=7

#finds prime, starting at 2
def finding_prime(num):
    for i in range(2, num):
        if (num % i ==0):
            return False
    return True

#starts prime number counter
#starts the current number at 2 and will end when
#number is hit

prime_num = 0
current_num = 1

#finds 10001st prime number
while(prime_num < 10001):
    current_num += 1
    if(finding_prime(current_num)==True):
        prime_num += 1

print(current_num)
