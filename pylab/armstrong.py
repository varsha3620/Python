num=int(input("enter a number:"))
temp=num
sum=0
while temp>0:
        digit=temp%10
        sum+=digit**len(str(num))
        temp=temp//10
if num==sum:
        print(f"{num} is an armstrong number")
else:
        print(f"{num} is not an armstrong number")



