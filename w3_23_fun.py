# def  flatten (l):
#     i=0
#     c=[]
#     while  i<len(l):
#         j=0
        
#         while j<len(l[i]):
#             c.append(l[i][j])
#             j=j+1
#         i=i+1
#     return c
# print(flatten([[2,4,3],[1,5,6], [9], [7,9,0]]))

            
            
# a=[[1,2,3],[4,5,6],[6,7,8],[8,9,0]]
# i=0
# c=[]
# while i<len(a):
#     j=0
    
#     while j<len(a[i]):
#         c.append(a[i][j])
#         j=j+1
#     i=i+1
# print(c)

def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()    
  return  uniq_items[1]   

print(second_smallest([1, 2, -8, -2, 0, -2]))
print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_smallest([2,2]))
print(second_smallest([2]))