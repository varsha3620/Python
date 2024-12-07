n=int(input("enter numbers of terms:"))
sum=0
num=[]
for i in range(n):
	n1=int(input("enter numbers:"))
	num.append(n1)
for i in num:
	sum+=i
print("sum of the list:",sum)
