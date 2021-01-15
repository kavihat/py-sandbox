# class Solution:
#     def compress(self, chars) -> int:
#         mdict={}
#         dict_list=''
#         for i in range(len(chars)):
#
#             if chars[i] in mdict:
#                 if mdict[chars[i]]=='':
#                     mdict[chars[i]]=1
#                 mdict[chars[i]]=mdict[chars[i]]+1
#             else:
#                 mdict.update({chars[i]:''})
#         chars=''
#         for k in mdict:
#             chars=str(chars)+str(k)+str(mdict[k])
#
#
#         return (chars)

# s=Solution()
# output=s.compress(["a","a","b","b","c","c","c"])
# print(output)

class Solution:
    def compress(self, chars) -> int:
        count = 0
        i = 0
        j = 0
        while i < len(chars):
            count = 1
            if len(chars) == 1:
                return 1

            for j in range(i,len(chars) - 1):
                if chars[j] == chars[j + 1]:
                    count =count+ 1
                else:
                    break

            print(count,j)

            if count == 1:
                i = i + 1
            elif count < 10:
                chars[i + 1] = str(count)
                # print(chars)
                # if count>1:
                del chars[i + 2:i + count]  # check this

                i = i + 2
            else:
                second = count % 10
                first = int(count / 10)
                chars[i + 1] = str(first)
                chars[i + 2] = str(second)
                del chars[i + 3:i + count]
                i = i + 3

                # char[i+1]=
        return (chars)


s = Solution()
output = s.compress(["a", "a", "b", "b", "b","a","a"])
print(output)
