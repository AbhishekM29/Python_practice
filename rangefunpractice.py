
mylist=[1,1,2,2,3,4,5,6]
count=0
duplicates =[]
for i in mylist:
    if mylist.count(i)>1:
        duplicates.append(i)
    elif duplicates.count(i)>1:
        duplicates.pop(i)
print(duplicates)








