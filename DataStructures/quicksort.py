def quicksort(ar, low, high):
    if low < high:
        pivot_index = partition(ar, low, high)
        quicksort(ar, low, pivot_index - 1)
        quicksort(ar, pivot_index + 1, high)


def partition(ar, low, high):
    i = low - 1
    print(low)
    print( i )
    pivot = ar[high]
    for j in range(low, high):
        if ar[j] < pivot:
            i = i + 1
            ar[i], ar[j] = ar[j], ar[i]
    ar[i + 1], ar[high] = ar[high], ar[i + 1]
    return (i + 1)
    # i = low
    # # print(low)
    # # print( i )
    # pivot = ar[high]
    # for j in range(low, high):
    #     if ar[j] < pivot:
    #         ar[i], ar[j] = ar[j], ar[i]
    #         i = i + 1
    # ar[i], ar[high] = ar[high], ar[i]
    # return (i)

# ar=[int(item) for item in input("Enter array").split(' ')]
ar = [5, 2, 1, 3,5,7,1,7,2,5,1,0]
quicksort(ar, 0, len(ar) - 1)
print(ar)
