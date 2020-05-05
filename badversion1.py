import random

n=int(input())    
get = random.randint(0,n) 
print(n,get)

def isbadversion(value):
    if value >= get:
        return True
    else:
        return False
def badversion(start ,end=n):

    mid = ((start+end)//2) 
    if isbadversion(mid)== True:
        if isbadversion(mid-1) == False:
            return mid
        else:
            return badversion(0,mid)
    else:
        return badversion(mid,n)

print(badversion(0,n))