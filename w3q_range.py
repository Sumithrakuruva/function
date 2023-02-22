# def count_range_in_list(li, min, max):
# 	ctr = 0
# 	for x in li:
# 		if min <= x <= max:
# 			ctr += 1
# 	return ctr

# list1 = [10,20,30,40,40,40,70,80,99]
# print(count_range_in_list(list1, 10, 100))

def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False
print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))



