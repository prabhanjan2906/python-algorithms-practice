inputstr = "abcabcbb"

def myfun(s):
    ans = set()
    finalans = set()
    startPtr = 0
    endPtr = 0
    answerLen = 0
    while endPtr < len(s):
        if s[endPtr] not in ans:
            ans.add(s[endPtr])
        else:
            if (answerLen < len(ans)):
                answerLen = len(ans)
                finalans = ans.copy()
            ans.remove(s[startPtr])
            startPtr += 1
            continue
        endPtr += 1
    print ("largest return value is ", len(ans) if len(ans)> len(finalans) else len(finalans), finalans)


myfun(inputstr)