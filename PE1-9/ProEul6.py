##https://projecteuler.net/problem=6

#sum of every number squared
sum_squares = 0
#sum of every number
sum = 0

#goes through 1-100
for i in range (1,101):
    #adds to sum
    sum += i
    #squares i and adds it
    sum_squares += i**2

#subtracts the square of the sum by the sumSquares 
result = sum**2 - sum_squares

#prints the difference
print (result)
