# prime factorization of a number

# naive solution



def isPrime(p):
    if(p==2 or p==3):
        return(True)
    elif(p%2==0 or p%3==0):
        return(False)
    else:
        ret=True
        for i in range(5,int(p**0.5)+1,6):
            if(p%i==0 or (p%(i+2))==0):
                ret=False
                break
        return(ret)

def primeFactorsRepeated(number,k): #for 12 [2,2,3] if k==2 then it returns 2,2  if 3 then it returns 3
    global OutList
    if(number%k==0):
        OutList+=[k]
        return(primeFactorsRepeated(number//k,k))
    else:
        return(number)



n=16
nCopy=n
OutList=[]
print()
print(OutList)
if(nCopy%2==0):
    nCopy=primeFactorsRepeated(nCopy,2)
if(nCopy!=1 and nCopy%3==0):
    nCopy=primeFactorsRepeated(nCopy,3)
if(nCopy!=1):
    for i in range(5,n+1):
        if(nCopy!=1):
            if(isPrime(i)):
                nCopy=primeFactorsRepeated(nCopy,i)
print(OutList)
        
            
            
            
