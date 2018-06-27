memoizer = {}

def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    return findminPathSum(grid, 0, 0)


def findminPathSum(grid, row, col):
    if (row >= len(grid)) or (col >= len(grid[row])):
        return -1

    if memoizer[(row, col)]:
        return memoizer[(row, col)]
    else:
        # i have 2 ways to go. down and right
        memoDown = findminPathSum(grid, row+1, col)
        memoRight = findminPathSum(grid, row, col+1)
        minSum = 0
        if (memoDown == -1) and (memoRight == -1):
            minSum = grid[row][col]
        elif (memoDown == -1):
            minSum = memoRight + grid[row][col]
        elif (memoRight == -1):
            minSum = memoDown + grid[row][col]
        else:
            minSum = memoDown if memoDown <= memoRight else memoRight
            minSum = minSum + grid[row][col]

        memoizer[(row, col)] = minSum # memoDown if memoDown <= memoRight else memoRight
        return minSum
