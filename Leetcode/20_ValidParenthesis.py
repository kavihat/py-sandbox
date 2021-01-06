s = "()"
stack=[]
dct={ '(':')','{':'}','[':']'}
i=0
while i<len(s):
    if s[i] in dct:
        stack.append(s[i])
    elif len(stack) >0 and dct[stack[len(stack)-1]]==s[i]:
        stack.pop()
    else:
        print("Not Valid")
    i+=1
if len(stack) == 0:
    print("valid")
else:
    print("not valid")
