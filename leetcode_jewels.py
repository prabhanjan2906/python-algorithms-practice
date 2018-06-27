from functools import reduce
J = "aAs"
S = "aaasssssADDDD"

jewels = set([J[i: i+1] for i in range(len(J))])

redFn = lambda count, data: count + 1 if data in jewels else count
shit = reduce (redFn, [S[i: i+1] for i in range(len(S))], 0)
print (shit)