num1=int(input("Enter a number"))
num2=int(input("Enter another number "))
operator=input("operation on two numbers")
if(operator=='+'):
  print(num1+num2)
elif(operator=='-'):
  print(num1-num2)
elif(operator=='*'):
  print(num1*num2)
elif(operator=='%'):
  print(num1%num2)
else: 
  print("invalid operator")
