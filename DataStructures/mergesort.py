def split(given_list):
    mid = len(given_list) // 2
    return given_list[:mid], given_list[mid:]


def merge(left_list, right_list):
    if len(left_list) == 0:
        return right_list
    elif len(right_list) == 0:
        return left_list
    index_left = index_right = 0
    list_merged = []
    len_target_list = len(left_list) + len(right_list)
    while len(list_merged) < len_target_list:
        if left_list[index_left] <= right_list[index_right]:
            list_merged.append(left_list[index_left])
            index_left += 1
        else:
            list_merged.append(right_list[index_right])
            index_right += 1
        if index_right == len(right_list):
            list_merged += left_list[index_left:]
            break
        elif index_left == len(left_list):
            list_merged += right_list[index_right:]
            break

    return list_merged


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left, right = split(arr)
        return merge(mergesort(left), mergesort(right))


arr = [5, 2, 1, 3, 5, 7, 1, 7, 2, 5, 1, 0]
print(mergesort(arr))