def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    splitstring = [s[i] for i in range(len(s))]
    myset = set(splitstring)
    if len(myset) == 1:
        return s
    matrix = []
    finalAns = ""
    for i in range(len(s)):
        matrix.append([False] * len(s))

    for strlen in range (0, len(s)):
        for i in range(0, len(s) - strlen):
            j = i + strlen
            if i == j: # 1 character
                matrix[i][j] = True
                finalAns = s[i:j+1]
            elif (s[i] == s[j]) and (j == i + 1): # 2 character string
                if matrix[i][j-1] == True:
                    matrix[i][j] = True
                    if (len(finalAns) < strlen + 1):
                        finalAns = s[i:j+1]
            else:
                if (s[i] == s[j]) and (matrix[i+1][j-1] == True):
                    matrix[i][j] = True
                    if (len(finalAns) < strlen + 1):
                        finalAns = s[i:j+1]
    if not (len(finalAns) == 1 and len(s) > 1):
        return finalAns

a = longestPalindrome('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
print(a)