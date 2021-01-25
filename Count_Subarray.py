def count_subarrays(arr):
    # Write your code here
    left = 0
    right = 0
    output=[]
    for i in range(0,len(arr)):
       right=i+1
       count=1
       while right <len(arr) and arr[i] > arr[right]:
           count+=1
           right+=1
       left=i-1
       while left >=0 and arr[i] > arr[left]:
           count+=1
           left -=1
       output.append(count)
    return output

dct={1:'a',2:'b'}
out=list(dct.values())
print(out)

print(count_subarrays([3, 4, 1, 6, 2]))
