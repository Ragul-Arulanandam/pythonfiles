Num =121
reverse = 0
rem = 0
while(Num>0):  
        reverse = reverse * 10 + (Num%10)
        Num = Num//10
if (reverse == Num):
    	print("The given number is palindrome")
		else:
    			print("The given number is not a palindrome")


