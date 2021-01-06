class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        orig = nums
        index = 0
        temp_index = 0
        if len(nums) < 2:
            pass
        else:
            i = len(nums) - 1
            while i > 0:
                if nums[i] > nums[i - 1]:
                    temp_index = i - 1
                    break
                i -= 1

            if i <= 0:
                nums.sort()
                return
            else:
                var = float('inf')
                for j in range(temp_index + 1, len(nums)):
                    if nums[j] > nums[temp_index]:
                        if var >= nums[j]:
                            var = nums[j]
                            index = j
                nums[temp_index], nums[index] = nums[index], nums[temp_index]
            nums[temp_index + 1:len(nums)] = reversed(nums[temp_index + 1:len(nums)])
