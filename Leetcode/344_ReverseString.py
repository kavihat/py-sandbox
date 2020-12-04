# class Solution:
#     def reverseString(self, s) -> None:
#         i=0
#         j=len(inp)-1
#         while i<=j:
#             s[i],s[j]=s[j],s[i]
#             i=i+1
#             j=j-1
#
#
#         return s
#
#
#
#
#
#
# s=Solution()
# inp=['h','e','l','l','o']
# inp=s.reverseString(inp)
# print(inp)

class Solution:
    def singleNumber(self, nums) -> int:
        dct = {}

        if len(nums) == 1:
            return nums[0]
        else:
            for i in nums:
                if i in dct:
                    dct[i] += 1
                else:
                    dct[i] = 1

        for item in dct:
            if dct[item] == 1:
                return item
s=Solution()
nums=[4,1,2,1,2]
inp=s.singleNumber(nums)
print(inp)
