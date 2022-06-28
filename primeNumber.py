# check if the given number is prime or not  ... 1 is neither prime nor composite. 2 is the only even prime


def isPrime(n):
    
    if(n==2 or n==3):
        return(True)
    elif(n%2==0 or n%3==0):
        return(False)
    else:
        ret=True
        for i in range(5,int(n**0.5)+1,6):  # prime should be checked till the square root cause above it there would be square
        # root of that number where the number surely fails if exist.
            if(n%i==0 or n%(i+2)==0):
                ret=False
                break
        return(ret)
    
print(isPrime(7))
        
