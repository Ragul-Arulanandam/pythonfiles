class Number:
    def __init__(self,number):
        try:
            self.num = int(number)
        except ValueError:
            raise ValueError

    def sum_of_number(self):
        Num = self.num
        sum =0
        while (Num>0):
            remainder = Num%10
            sum = sum+int(remainder)
            Num = Num/10
        return sum

    def is_palindrome(self):
        Num = self.num
        #rem = 0
        reverse = 0
        while(Num>0):
            rem = Num%10 
            reverse = reverse * 10 + rem
            Num = Num//10
        if (reverse == self.num):
            return "The given number is palindrome"
        else:
            return "The given number is not a palindrome"

    def product_value(self):
        Num = self.num
        product =1
        while (Num!=0):
            product = product * int(Num%10)
            Num = Num//10
        return product

    def square_value(self):
        Num = self.num
        Result = Num * Num 
        return Result
    def negative_value(self):
        Num = self.num
        return -Num 






    
