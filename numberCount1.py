# Project euler problem 1. Find the sum of all the numbers from 1 to 1000
# which are multiples of 3 or 5
x=0
n = 1000
while x < n:
        if x % 3 == 0 or x % 5 == 0:

                result = result + x
        x = x+1

print "Final RESULT"
print result



