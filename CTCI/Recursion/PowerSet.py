output=[]
def powerSet(arr):
    subset(arr,[],0)
    return output

def subset(arr,curr_arr,index):
    if index==len(arr):
        output.append(curr_arr)
    else:
     subset(arr,curr_arr,index+1)
     subset(arr,curr_arr+([arr[index]]),index+1)


print(powerSet([1,2,3]))