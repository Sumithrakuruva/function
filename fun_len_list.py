# def count(l):
#     c=0
#     for i in l:
#         # print(i)
#         c=c+1
#     return c
# print(count([1,2,3,4,5,6,7,1,23,4]))


# def  count(l):
#     c=0
#     i=0
#     while i<len(l):
#         c=c+1
#         i=i+1
#     return c
# print(count([1,2,3,4,5,6,7,8,9,1]))


def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()