# WAP to find greatest among two numbers
num1=int(input("enter 1st number"))
num2=int(input("Enter 2nd number"))
greter=0
if num1>num2:
    greter=num1
else:
    greter=num2
print("Greter number between ",num1,"And ",num2, " is ", greter)