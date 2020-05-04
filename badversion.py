import random

n=int(input())
def isbadversion(n):
    Number = random.randint(0,n)   
    return Number     

print(isbadversion(n))

def badversion(n):
    l=0
    r=n-1
    min = 0
    while l<=r:
        mid = (l+r)//2
        get = isbadversion(n)
        if get == mid:
            return mid #"good versions"
        elif get>mid:
            l=mid+1
        else:
            l=mid-1

    return mid

print(badversion(n))