"""
Find Lucky Integer in an Array
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
"""

class Solution:
    def findLucky(self, arr) -> int:
        my_dict = {}
        maxlist = []
        for i in range(len(arr)):
            if arr[i] in my_dict:
                my_dict[arr[i]] = my_dict[arr[i]] + 1
            else:
                my_dict[arr[i]] = 1
        for k in my_dict:
            if k == my_dict[k]:
                maxlist.append(my_dict[k])
            else:
                continue
        if maxlist!=[]:
            return max(maxlist)
        else:
            return -1

s=Solution()
final=s.findLucky([1,1,2,3])
print(final)



