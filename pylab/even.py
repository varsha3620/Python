n=int(input("enter numbers of integers to input:"))
listed=[]
for i in range(n):
	num=int(input("enter integers:"))
	if num%2!=0:
		listed.append(num)
print(f"Newlist:{listed}")
