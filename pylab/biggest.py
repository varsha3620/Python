num1=int(input("enter first number:\n"))
num2=int(input("enter second number:\n"))
num3=int(input("enter third number:\n"))
if num1>num2&num1>num3:
    print(f"{num1}is biggest number")
elif num2>num3:
   print(f"{num2}is biggest number")
else:
    print(f"{num3}is biggest number")
