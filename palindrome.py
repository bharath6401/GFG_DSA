# palindrome check

def isPalindrome(n):
    if(str(n)[::-1]==str(n)):
        return(True)
    else:
        return(False)

print(isPalindrome(212))



def isPalindrome(n):
    number=n
    temp=0
    while(number>0):
        lastDigit=number%10
        temp=temp*10+lastDigit
        number//=10
    return(n==temp)
    
    
print(isPalindrome(212))
