from random import randint
import sys

answer = randint(1,10)

while(1):
    print(answer)
    guessing_number = int(input("Enter the guessing number"))
    try:
        if 0<guessing_number<11:
            if guessing_number == answer:
                print("Ragul you're correct!! :)")
                break
        else:
            print("Enter the number with in range...")
            break
    except ValueError:
        print("Enter an integer value!")
        continue       
    