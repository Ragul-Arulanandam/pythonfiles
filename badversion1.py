import random

n=int(input())    
get = random.randint(0,n) #5

def isbadversion(value):
    if value == get:
        return True
    else:
        return False
def badversion(start ,end=n):
    
    mid = ((start+end)//2) #5

    while start<=end:
        if get<=0:
            return "No good version is available"
        else:
            if isbadversion(mid)== True:
                if isbadversion(mid-1) == False:
                    return mid
                else:
                    return badversion(0,mid)
            else:
                return badversion(mid,n)

print("The badversion is ",badversion(0,n))