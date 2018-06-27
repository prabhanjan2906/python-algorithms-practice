dp = []


def lookForTrueInPreviousRow(row):
    for i in range(len(row)):
        if (row[i]) == True:
            return True
    return False

def walkTree(i, j):
    count = 0
    while ((i >= 0) and (j >= 0)):
        if (dp[i][j] == True):
            if (i == 0):
                count = count + 1
            else:
                count = count + walkTree(i - 1, j - 1)
        j = j - 1
    return count

def numDistinct(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    for i in range(len(t)):
        dp.append([False] * len(s))

    for i in range(len(t)):
        for j in range(len(s)):
            if (t[i] == s[j]):
                # look for a row before
                if i -1 < 0:
                    dp[i][j] = True
                else:
                    dp[i][j] = lookForTrueInPreviousRow(dp[i-1][:j])

    return walkTree(len(t) - 1, len(s) - 1)

cnt = numDistinct(None, "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe", "bddabdcae")
print (cnt)