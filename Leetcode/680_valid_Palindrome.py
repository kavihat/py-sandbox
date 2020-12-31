s="eddboebddcaacddkbebdde"
i=0
size=len(s)-1
j=len(s)-1
flag=1
count=0
dct={}
prev_i=0
prev_j=0
memo=False
final=False
dct={}
print(len(s))
# for i in range(len(s)):
#     dct[s[i]]=s.count(s[i])
# print(dct)
while i<j:
    if (s[i]==s[j] and count<=1) :
            i+=1
            j-=1
            print("here1")
    elif s[i]!=s[j] and count==0:
        print("here2")
        count+=1
        if s[i+1]==s[j]:
            memo=True
            prev_i=i
            prev_j=j
            i += 1
            continue
        else:
            j-=1
    elif s[i]!=s[j] and memo==True and count==1 and final==False:
        print("here3")
        i=prev_i
        j=prev_j
        j-=1
        final=True
    else:
        print("here5")
        flag=0
        break
if flag==0:
   print(False)
else:
    print(True)
