ar=[int(item) for item in input('Enter the numbers to be sorted').split(' ')]
for i in range(0,len(ar)-1):
    # cur=ar[i]
    while(i>=0):
        if ar[i]>ar[i+1]:
            temp=ar[i]
            ar[i]=ar[i+1]
            ar[i+1]=temp
            i=i-1
        else:
            i=i-1

print(*ar, sep=' ')