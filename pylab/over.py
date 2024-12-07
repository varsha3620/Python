n=int(input("enter numbers of integers to input:"))
list1=[]
for i in range(n):
	num=int(input("enter integers:"))
	if num>100:
		num="over"
	list1.append(num)
print(list1)
