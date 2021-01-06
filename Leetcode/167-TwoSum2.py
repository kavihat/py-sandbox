numbers = [-1,0]
target=-1
m={}
def twosum(numbers):
    for i in range(len(numbers)):
        if target-numbers[i] in m:
            if i+1 > m[target-numbers[i]]:

                return [m[target-numbers[i]],i+1]
            else:
                return [i+1,m[target - numbers[i]]]
        else:
            m[numbers[i]]=i+1

ans=twosum(numbers)
print(ans)
