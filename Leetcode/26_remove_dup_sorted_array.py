nums=[0,0,1,1,1,1,2,3,3]
i=0
while True:
    if i < len(nums)-2:
        if nums[i]==nums[i+2]:
            del nums[i+1]
        else:
            i=i+1
    else:
        break

print(nums)