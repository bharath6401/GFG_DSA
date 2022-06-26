# Counting no of digits in a number

# iterative approach

n=12345
count=0
while(n>0):
    n//=10
    count+=1
print(count) 

# recursive approach

def countDigits(num):
    if(num==0):
        return(0)
    return(1+countDigits(num//10))
print(countDigits(1234))


# by using logorithm
import math
n=123
print(math.floor(math.log(n,10))+1)


    
