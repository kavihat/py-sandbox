# program to return the indexes of the pair of numbers in the list whose sum is the inputed targer sum

# class Solution:
#     def twoSum(self, nums, target: int):
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] + nums[j] == target and i != j:
#                     return i,j
#
#
# s=Solution()
# first,second= s.twoSum([2, 7, 11, 15],9)
# print('['+str(first)+','+str(second)+']')

# class Solution:
#     def twoSum(self, nums, target: int):
#         for i in range(len(nums)):
#                 if target-nums[i] in nums:
#
#                 else:
#                     i=i+1
#
#         return i,nums.index(target-nums[i])
#
#
# s=Solution()
# first,second =s.twoSum([3,2,4],6)
# print(first,second)

class Solution:
    def twoSum(self, nums, target: int):
        m = {}
        # out=[]
        # nums = [1, 2, 3, 4]
        # target = 6
        for i in range(len(nums)):
            if target - nums[i] in m:
                # out.append(i,m[i])
                return [m[target - nums[i]], i]
            else:
                m[nums[i]] = i
                i = i + 1


s = Solution()
out = s.twoSum([1, 2, 3, 4], 3)
print(out)
