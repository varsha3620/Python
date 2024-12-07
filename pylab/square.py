squareevenlist=[]
for i in range(32,100):
        square=i*i
        if 1000 <= square <= 9999:
                isalleven=True
                temp=square
                while temp>0:
                        digit=temp%10
                        if digit%2!=0:
                                isalleven=False
                                break
                        temp//=10
                if isalleven:
                        squareevenlist.append(square)
print(f"Four digit perect square with all even disgits:{squareevenlist}")





