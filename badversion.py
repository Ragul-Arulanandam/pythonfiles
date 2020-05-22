import random

n= int(input())

def badversion(n):
    start=0
    end=n-1
    get = random.randint(0,n)
    print("the fail",get)
    while start<=end:
        mid = (start+end)//2
        if get <=0:
            return "no good version"
        else:
            if get == mid:
                return mid #"good versions"
            elif get>mid:
                start=mid-1
            else:
                start=mid+1

    return mid

print(badversion(n))