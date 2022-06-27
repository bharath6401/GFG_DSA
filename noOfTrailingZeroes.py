# no of trailing zeroes in the factorial of the given number .
# [n//5]+[n//25]+[n//125] just counting no of 5's in prime factorization of the factorial numbers.

n=25
nCopy=n
powersOfFive=5
noOfTrailingZeroes=0
while(n>=powersOfFive):
    noOfTrailingZeroes+=n//powersOfFive
    powersOfFive*=5
    
print(noOfTrailingZeroes)
    
