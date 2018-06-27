from functools import reduce
nums = [1,4,3,2]
nums.sort()
sum = reduce(lambda x, y: x + y, nums[0::2])
print (sum)
