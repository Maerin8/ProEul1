##https://projecteuler.net/problem=4

# function which return reverse of a string
 
def isPalindrome(s):
    return s == s[::-1]

# highest number multiple
highest = 0

# goes from 999 to 0 for both multiples
for ii in range(999, 0, -1):
    for jj in range (999, 0, -1):
        print(ii," * ",jj," = ",ii * jj)
        #prints multiples and checks if it is a palindrome
        s = str(ii * jj)
        ans = isPalindrome(s)
        
        #if it is a palindrome, check if it is highest
        if ans:
            if (ii * jj) > highest:
                highest = ii * jj

#print highest found
print(highest)
