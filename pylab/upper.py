limit=int(input("enter the upper limit:"))
total=0
for num in range(1,limit):
        if num%6==0 and num%4!=0:
                total+=num
print("sum:",total)

