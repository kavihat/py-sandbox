strs = ["flower", "flow", "flight"]
if not strs:
    print('')

minstr = min(strs, key=len)  # find the str with smallest length
i = 0
flag = True
out=[]
while i < len(minstr):
    for x in strs:
        if x[i] == minstr[i]:
            continue
        else:
            flag = False

    if flag == False:
        break
    i += 1

print( minstr[:i])
