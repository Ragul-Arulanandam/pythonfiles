import re

Userinput = str(input("Your regiester number "))

Separated_input = Userinput.split("-")
print(Separated_input)

College_code1 = re.compile(str(Separated_input[0]))
print(College_code1)

with open ('college_code.txt') as CollegeCode:
    self1 =CollegeCode.readlines()
    CollegeCode1=tuple(self1)
    print(CollegeCode1)

#a = College_code1.search(CollegeCode1)
#print(a)

