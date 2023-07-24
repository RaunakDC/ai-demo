from add import *
from sub import *

num1= int(input("Enter first number:"))
num2= int(input("Enter second number:"))

add1=add(num1,num2)
sub1=sub(num1,num2)

print(f"The addition of {num1} and {num2} is {add1}")
print(f"The subtarction of {num1} and {num2} is {sub1}")

