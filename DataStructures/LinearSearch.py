# Linear Search

input_list = [int(i) for i in input('Enter list of numbers').split(' ')]
item = int(input('Enter the element you have to search'))
for i in range(len(input_list)):
       if input_list[i] == item:
            print('Item found at ', i+1)
            break
       else:
            i = i + 1
