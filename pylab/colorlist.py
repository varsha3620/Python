list1=input("enter colors for list1 seperated by comma:")
list2=input("enter colors for list2 seperated by comma:")
set1=set(list1.split(','))
set2=set(list2.split(','))
difference=set1-set2
print("colors in list1 but not in list2:",difference)






