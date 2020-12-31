nums=[0]
i=0
while True:
    if i < len(nums)-1:
        if nums[i]==0:
            nums.insert(i+1,0)
            nums.pop()
            i=i+2
        else:
            i=i+1
    else:
        break
print(nums)
