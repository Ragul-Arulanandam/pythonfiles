'''N = int(input("Enter the number of terms"))

a = 0
b =1
c = 0

if N<=0:
    print("Enter the valid number")
elif N==1:
    print(b)
else :
    while c<N:
        print(a)
        nth=a+b
        a=b
        b=nth
        c=c+1'''



def fib_series(n):
    a=0
    b=1
    for i in range (n) :
        yield a
        temp =a+b
        a=b
        b=temp
n=int(input("Enter the fib range"))
for x in fib_series(n):
    print(x)