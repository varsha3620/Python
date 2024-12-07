str=input("enter the list of words sperated by space:")
words=str.split()
length=0
for i in words:
    if len(i)>length:
        longestword=i
        length=len(i)
print(f"longestword is {longestword} and its length is {length}")
