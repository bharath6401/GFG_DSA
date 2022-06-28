# gcd of two numbers  .  max square length made from a rectangle of l*w dimensions.

def gcd(a,b):
    if(b==0):
        return(a)
    return(gcd(b,a%b))




# lcm of two numbers .  disco lights light together after how long if they light at 2,3 sec intervals.
# from the formulae  product of two numbers=product of their gcd and its lcm==>{a*b=gcd(a,b)*lcm(a,b)}

def LCM(a,b):
    return((a*b)/gcd(a,b))
print(LCM(5,4)) #always a>b
