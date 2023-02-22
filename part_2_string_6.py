# a="the quick brown fox jumps over the lazy dog"
# b=a.split()
# print(b)
# i=0
# d=[]
# while i<len(b):
#     c=d.count(b[i])
    
    
def permute(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms

my_nums = [1,2,3]
print("Original Cofllection: ",my_nums)
print("Collection of distinct numbers:\n",permute(my_nums))

