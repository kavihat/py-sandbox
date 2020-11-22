"""
1304Find N Unique Integers Sum up to Zero
"""


class Solution:
    def sumZero(self, n: int):
        ar = []
        end = n // 2
        for i in range(1, end + 1):
            ar.append(i)
            ar.append(-i)
        if n % 2:
            ar.append(0)
        return ar


s = Solution()
output = s.sumZero(8)
print(output)
