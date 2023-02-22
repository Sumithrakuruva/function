def change(a):
    for i in range (0,len(a),2):
        (a[i],a[i+1])=(a[i+1],a[i])
    return a
    # a=[0,1,2,3,4,5]
print(change([0,1,2,3,4,5]))

    