'''def is_even(a):
    if a%2==0:
        return True
    else:
        return False

print(is_even(9))
print(is_even(2))'''

'''list(range(100))
def make_list(num):
    result=[]
    for i in range(num):
        result.append(i*3)
    return result

my_list=make_list(100)
print(my_list)'''


def Productvalue(Num):
        Num = self.num
        rem = 0
        product =0
        while (Num>0):
            rem = Num%10
            product = product * int(rem)
            Num = Num/10
        return product

p = Productvalue(123)
print(p)