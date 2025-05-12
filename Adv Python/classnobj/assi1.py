"""Q.1)Calculator Class

Create a Calculator class with methods to perform basic arithmetic operations:

add, subtract, multiply, divide."""

class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def addition(self):
        return self.num1+self.num2
    
    def substract(self):
        return self.num1-self.num2
    
    def multiply(self):
        return self.num1*self.num2
    
    def divide(self):
        return self.num1//self.num1
    
num1=int(input("Enter 1st number "))
num2=int(input("Enter 2nd number "))
ob=calculator(num1,num2)
print(f'Addition of this number is {ob.addition()}')
print(f'substraction of this number is {ob.substract()}')
print(f'Multiplication of this number is {ob.multiply()}')
print(f'Division of this number is {ob.divide()}')