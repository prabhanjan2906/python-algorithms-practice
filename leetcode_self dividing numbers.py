from functools import reduce

left = 1
right = 22

def checker (count, num):
    for c in str(num):
        if (int(c) == 0 or (num % int(c) != 0)):
            return count
    count.append(num)
    return count

s = reduce(checker,
           [i for i in range(left, right + 1)],
           [])
print (s)