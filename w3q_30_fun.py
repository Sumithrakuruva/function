def frequeny(a):
    i=0
    f=[]
    while i<len(a):
        e=[]
        c=a.count(a[i])
        e.append(a[i])
        e.append(c)
        if e not in f:
            f.append(e)
        i=i+1
    return f
print(frequeny([10,10,10,10,20,20,20,20,40,40,50,50,30]))