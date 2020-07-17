input_list = [int(i) for i in input('Enter sorted array').split(' ')]
item = int(input('Enter the item to search'))
left = 0
loc = 0
right = len(input_list) - 1
while right >= left:
    mid = left + (right - left) // 2
    if input_list[mid] == item:
        loc = mid
        break
    elif input_list[mid] > item:
        right = mid - 1
    else:
        left = mid + 1
if loc == 0:
    print('Item not found')
else:
    print('item found at : ', loc + 1)
