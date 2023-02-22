list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
i=0
b=[]
c=[]
while i<len(list1)-1:
    if list1[i] not in list2:
        b.append(list1[i])
    if list2[i] in list1:
        c.append(list2[i])
    i=i+1
b.extend(c)
print(b)