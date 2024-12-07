def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul a*b:
	return a*b
def div(a,b):
	if b!=0
		return a/b
	else
		return"error!division by zero"
	a=float(input("enter a number1:"))
	b=input("enter a number2:")
	while True:
		print("1.Addition")
		print("2.subtraction")
		print("3.multiplication")
		print("4.division")
		print("5.fail")
		choice=input("Enter choice")
	if choice='5'
		print("Exiting the calculator")
		break
	if choice in ['1','2','3','4']:
		if choice=='1':
			print("f{a}+{b}={add(a,b)}")
		if choice=='2':
			print("f{a}-{b}={sub(a,b)}")
		if choice=='3':
                        print("f{a}*{b}={mul(a,b)}")
                if choice=='4':
                        print("f{a}/{b}={div(a,b)}")
              else:
			print("inavlid choice!Tryagain")

