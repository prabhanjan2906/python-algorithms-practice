import math
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    lenX = len(nums1)
    startX = 0
    endX = lenX
    return findMedian(nums1, nums2, startX, endX-1)

def findMedian(nums1, nums2, startX, endX):
    lenX = len(nums1)
    lenY = len(nums2)
    numberOfItemsOnLeftPartitionOfX = int((startX + endX)/2)
    numberOfItemsOnLeftPartitionOfY = int(((lenX + lenY + 1)/2)) - numberOfItemsOnLeftPartitionOfX
    isTotalNumberOfElementsIsEven = True if (lenX + lenY) % 2 == 0 else False

    leftX, rightX = splitArrayIntoPartitions(nums1, numberOfItemsOnLeftPartitionOfX)
    leftY, rightY = splitArrayIntoPartitions(nums2, numberOfItemsOnLeftPartitionOfY)

    maxLeftX = leftX[-1] if len(leftX) > 0 else -math.inf
    minRightX = rightX[0] if len(rightX) > 0 else math.inf
    maxLeftY = leftY[-1] if len(leftY) > 0 else -math.inf
    minRightY = rightY[0] if len(rightY) > 0 else math.inf
    if ((maxLeftX <= minRightY)):
        if (maxLeftY <= minRightX):
            if (isTotalNumberOfElementsIsEven):
                avg = getMaxNumber(maxLeftX, maxLeftY) + getMinNumber(minRightX, minRightY)
                return avg/2
            else:
                return getMaxNumber(maxLeftX, maxLeftY)
        else:
            return findMedian(nums1, nums2, numberOfItemsOnLeftPartitionOfX + 1, endX)
    else:
        return findMedian(nums1, nums2, startX, numberOfItemsOnLeftPartitionOfX)

def splitArrayIntoPartitions(arr, indexToSplit):
    return  (arr[: indexToSplit], arr[indexToSplit:])

def getMinNumber(a, b):
    return a if a <= b else b

def getMaxNumber(a, b):
    return a if a >= b else b

a = [23, 26, 31, 35]
b = [3, 5, 7, 9, 11, 16]
c = [1, 3, 8, 9, 15]
d = [7, 11, 18, 19, 21, 25]
e = [1, 2]
f = [3, 4]
median = findMedianSortedArrays(e, f)
print (median)