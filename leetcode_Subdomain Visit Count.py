hsh = {}

def myFunc(inputStrArr):
    print(inputStrArr)
    (count, myString) = inputStrArr.split(' ')
    count = int(count)
    if myString in hsh:
        hsh[myString] = hsh[myString] + count
    else:
        hsh[myString] = count

    pos = myString.find('.')

    while (pos != -1):
        myString = myString[pos + 1:]
        if myString in hsh:
            hsh[myString] = hsh[myString] + count
        else:
            hsh[myString] = count
        pos = myString.find('.')

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
for domain in cpdomains:
    myFunc(domain)

finalAns = []
for k,v in hsh.items():
    s = str(v) + " " + str(k)
    finalAns.append(s)

print (finalAns)