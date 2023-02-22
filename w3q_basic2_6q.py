# a="the quick brown fox jumps over the lazy dog"
# b=a.split()
# print(b)
# i=0
# f=[]
# while i<len(b):
#     e=[]
#     c=b.count(b[i])
#     e.append(b[i])
#     e.append(c)
#     if e not in f:
#         f.append(e)
#     i=i+1
# print(f)

t=int(input())
while t>0:
    a=list(map(int,input().split()))
    a.sort()
    print(a[-2])
    t=t-1
