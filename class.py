'''class Game:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print("Run")
        return "Gameover"

p1=Game("Ragul",20)
print(p1.name,p1.age,p1.run())'''
    

class Cat:
    def __init__(self,name,age):
        self.name=name #attributes are features or proberties of a variables
        self.age=age

cat1=Cat("rocky", 20) #declaring cat1 
cat2=Cat("rock", 23) #declaring cat2

print(cat1.name)
print(cat1.age) #methods which is used to function something they 
                            #operation of the variables.

def oldest_cat(*args):
    return max(args)

print(oldest_cat(cat1.age,cat2.age))
