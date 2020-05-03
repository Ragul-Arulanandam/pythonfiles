from calciModule import *
 

operations = { 1: "Addition",
                2: "Subraction",  
                3: "Multiplicatin",
                4: "Division"
                }
print(operations)
User_input=int(input("Enter the operation"))
a = int(input("Enter the number a"))
b = int(input("Enter the number b"))
operationType = operations[User_input]
try:
    if (operationType =="Addition"):
        print(sum(a,b))
    elif (operationType == "Subraction"):
        print(sub(a,b))
    elif (operationType == "Multiplication"):
        print(mul(a,b))
    elif (operationType == "Division"):
        print(div(a,b))
    else:
        print("Enter the valid operation")

except TypeError:
    print("Valid numbers")
except:
    print("syntax error")
