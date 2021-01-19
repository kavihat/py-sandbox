def BinarySearch(nums, start=0, end=0):
    if end < start:
        return None
    else:
        mid = (start + end) // 2

        if nums[mid] == mid:
            print("mid", mid)
            return mid
        elif nums[mid] > mid:

            BinarySearch(nums, 0, mid - 1)
        else:

            BinarySearch(nums, mid + 1, end)


nums = [-11, -2, 1, 3, 50]
print(BinarySearch(nums, 0, len(nums) - 1))
