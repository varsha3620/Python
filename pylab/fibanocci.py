num=int(input("Enter the number of terms:"))
a,b=0,1
for i in range(num+1):
	print(a,end=" ")
	c=a+b
	a,b=b,c
