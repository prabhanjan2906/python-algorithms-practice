import math
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    highLimit = math.pow(2, 31) - 1
    lowLimit = -1 * math.pow(2, 31)
    neg = True if x < 0 else False
    if neg:
        x = -1 * x
    reversedNum = 0
    while x > 0:
        reversedNum = (reversedNum * 10) + x % 10
        x = int(x / 10)

    reversedNum = reversedNum if not neg else -1 * reversedNum
    if (reversedNum > highLimit) or (reversedNum < lowLimit):
        return 0
    return reversedNum

print (reverse(-9646324351))