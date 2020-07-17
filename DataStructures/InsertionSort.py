input_list = [int(i) for i in input('Enter the numbers to be sorted').split(' ')]
for i in range(1, len(input_list)):
    j=i
    while j > 0 and input_list[j - 1] > input_list[j]:
            temp = input_list[j - 1]
            input_list[j - 1] = input_list[j]
            input_list[j] = temp
            j = j - 1

print(*input_list, sep=' ')