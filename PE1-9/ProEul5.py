#https://projecteuler.net/problem=5

def isDivisible(num):
    for i in range(1, 21):
        if num % i != 0:
            return False
    return True

num = 20 #starting number
while True:
    if isDivisible(num):
        break
    print("{:,}".format(num))
    num+=20 #add by 20 since it has to be divisible by 20
		#makes it run 20x faster
print("We've found", num)
