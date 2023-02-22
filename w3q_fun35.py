def mutply(a):
    i=0
    b=[]
    d=[]
    while i<4:
        c=a[0]+str(i+1)
        e=a[1]+str(i+1)
        i=i+1
        b.append(c)
        d.append(e)
    b.extend(d)
    return b
print(mutply(["p","q"]))