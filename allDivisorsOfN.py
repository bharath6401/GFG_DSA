# find all the divisors of the given number

# sorted solution

def getAllDivisorsOfN(n):
    global divisorsList
    for i in range(1,int(n**0.5)+1):
        if(n%i==0):
            divisorsList+=[i]
    for i in range(int(n**0.5)+1,0,-1):
        if(n%i==0):
            divisorsList+=[n//i]


divisorsList=[]
n=15
getAllDivisorsOfN(n)

    
print(divisorsList)

# unsorted  Solution

def getAllDivisorsOfN(n):
    global divisorsList
    for i in range(1,int(n**0.5)+1):
        if(n%i==0):
            divisorsList+=[i]
            divisorsList+=[n//i]
    


divisorsList=[]
n=18
getAllDivisorsOfN(n)

    
print(divisorsList)
