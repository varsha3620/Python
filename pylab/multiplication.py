n=int(input("Enter a number:"))
m=int(input("enter a limit:"))
print("multiplication Table:")
for i in range(1,m+1):
	mul=i*n
	print(f"{i}*{n}={mul}")
