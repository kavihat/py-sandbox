# s="abcabcdbb"
# i=0
# res=[]
# dct={}
# while True:
#     if i<len(s):
#         if s[i] not in res:
#             res+=s[i]
#             i=i+1
#         else:
#             tp=tuple(res)
#             dct[tp]=len(res)
#             res=[]
#     else:
#         break
# print(dct)

s=""
i=0
dct={}
size=0
max=0
while i <len(s):
        if s[i] not in dct:
            size+=1
            dct[s[i]] = i
            i=i+1

        else:
            if size>max:
                max=size
            i=dct[s[i]]+1
            dct={}
            size=0
if size > max:
    max = size
