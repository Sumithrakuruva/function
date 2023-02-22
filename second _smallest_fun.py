a=[1, 2, -8, -2, 0, -2]
i=0
b=[]
min=a[0]
max=a[0]
while i<len(a):
    if a[i]<min:
        min=a[i]
    i=i+1
j=0
while  j<len(a):
    if a[j]<max and a[j]!=min:
       max=a[j]
    j=j+1
# print(min)
print(max)
                    
