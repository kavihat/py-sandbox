nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]

n = 3


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        write = len(nums1) - 1
        read1 = m - 1
        read2 = n - 1
        while read2 >= 0 or read1 >= 0:
            if read1 < 0 or (read2 >= 0 and nums2[read2] >= nums1[read1]):
                nums1[write] = nums2[read2]
                read2 -= 1
                write -= 1
            else:
                nums1[write] = nums1[read1]
                read1 -= 1
                write -= 1

#####################################ALTERNATE SOLUTION (O(NLOGN))
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

# if len(nums1) !=0 and len(nums2)!=0:
#             var1=[str(x) for x in nums1]
#             var1=int("".join(var1))
#             var2=[str(x) for x in nums2]
#             var2 = int("".join(var2))
#             var1=var1+var2
#             nums1=[int(x) for x in str(var1)]
#             nums1.sort()
# elif len(nums2)==0:
#              pass
# print(nums1)