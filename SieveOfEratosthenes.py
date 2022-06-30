# sieve of eratosthenes

# way to find prime numbers in a range 

n=10

isPrime=[True]*n 


for i in range(2,n):
    if(isPrime[i]):   #the current number would be true if only if it is not divisible by any of the previous numbers
    # in the list which makes it obvious that it is prime.
        j=i*i #ignores the current element as its prime
        for j in range(j,n,i): 
            isPrime[j]=False
print(isPrime)

primes=[i for i in range(len(isPrime)) if(isPrime[i])]
print(primes[2:])#trim off  0 and 1
        
    
