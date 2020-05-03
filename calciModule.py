try:
    def sum(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def mul(x,y):
        return x*y
    def div(x,y):
        quotient = x/y
        remainder = x%y
        return quotient,remainder

except ZeroDivisionError:
    print("syntax error")