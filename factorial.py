# factorial of a number

# recursive solution

def factorial(n):
    if(n==1):
        return(1)
    return(n*factorial(n-1))


print(factorial(3))



# iterative solution

n=4
result=1
for i in range(2,n+1):
    result*=i 
print(result)
    
