from functools import reduce

u = r = 1
d = l = -1

inputStr = "LL"

pos = (0, 0)
for c in range(len(inputStr)):
    if (inputStr[c] == "U"):
        pos = (pos[0] + u, pos[1])
    elif (inputStr[c] == "D"):
        pos = (pos[0] + d, pos[1])
    elif (inputStr[c] == "L"):
        pos = (pos[0], pos[1] + l)
    elif (inputStr[c] == "R"):
        pos = (pos[0], pos[1] + r)
if (pos == (0, 0)):
    print ("shit nigga")
else:
    print ("smart ass nigga")