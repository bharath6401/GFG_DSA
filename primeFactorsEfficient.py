
# print all prime factors of a number

# naive solution

def primeFactors(n):
    global primeFactorsList
    for i in range(2,n+1):
        
        while(n%i==0):
            primeFactorsList+=[i]
            n=n//i 
   
        
primeFactorsList=[]
            
primeFactors(20) 
print(primeFactorsList)




# efficient solution

def primeFactors(n):
    global primeFactorsList
    for i in range(2,int(n**0.5)+1):
        
        while(n%i==0):
            primeFactorsList+=[i]
            n=n//i 
    if(n>1):
        primeFactorsList+=[n]
        # print(n)
        
primeFactorsList=[]
            
primeFactors(15) 
print(primeFactorsList)


# more efficient approach. we use the same logi as we did for prime numbers. 



def primeFactors(n):
    global primeFactorsList
    
    if(n>1):
        while(n%2==0):   #we handle i==2 and i==3 explicitely which enable us to increment by 6
                primeFactorsList+=[2]
                n=n//2
        while(n%3==0):
                primeFactorsList+=[3]
                n=n//3
        
        for i in range(5,int(n**0.5)+1,6):
            while(n%i==0):
                primeFactorsList+=[i]
                n=n//i 
            while((n%(i+2))==0):
                primeFactorsList+=[i+2]
                n=n//(i+2)
        if(n>1):
            primeFactorsList+=[n]
            # print(n)
        
primeFactorsList=[]
            
primeFactors(15) 
print(primeFactorsList)









