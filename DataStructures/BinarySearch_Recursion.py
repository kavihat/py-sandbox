def binary_search(elements, item, minimum, maximum):
    if maximum >= minimum:
        mid = (maximum + minimum) // 2
        # print(mid)
        if elements[mid] == item:
            return mid

        elif elements[mid]>item:
            return binary_search(elements, item, minimum, mid-1)
        else:
            return binary_search(elements, item, mid+1, maximum)
    else:
        return


# input_list = [int(i) for i in input('Enter sorted array').split(' ')]
# item_to_search = int(input('Enter the item you want to search'))
input_list = [1, 2, 3]
item_to_search = 1


loc = binary_search(input_list, item_to_search, 0, len(input_list)-1)
if loc is not None:
    print('Item found at position: ', loc+1)
else:
    print('Item  not found!')
