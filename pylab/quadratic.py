import math
print("Quadratic equation: ax**2+bx+c=0")
a=int(input("enter (a!=0):"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=(b**2)-(4*a*c)

if d>0:
  root1=(-b+math.sqrt(d))/(2*a)
  root2=(-b-math.sqrt(d))/(2*a)
  print(f"the equation has two distinct real roots:{root1}and{root2}")
  
elif d==0:
  root=-b/(2*a)
  print("The equaton has two equal root:{root}")
else:
  realpart=-b/(2*a)
  imaginarypart=math.sqrt(-d)/(2*a)
  print(f"the equation has two complex roots:{realpart}+{imaginarypart}i and {realpart}-{imaginarypart}i")
