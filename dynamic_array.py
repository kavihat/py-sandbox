# Dynamic array class - Data Structure


class DynamicArray:
    def __init__(self):
        self.array = [0] * 2
        self.current_index = 0
        self.capacity = 2

    def __str__(self):
        is_first = True
        j = self.current_index
        string = '['

        while j > 0:
            for i in self.array:
                if is_first:
                    string += str(i)
                    is_first = False
                    j = j - 1
                elif j == 0:
                    break
                else:
                    string += ',' + str(i)
                    j = j - 1
        string = string + ']'
        return string

    def __len__(self):
        return self.current_index

    def add(self, item):
        if self.current_index + 1 == self.capacity:
            self.resize()
            self.array[self.current_index] = item
            self.current_index += 1

        else:
            self.array[self.current_index] = item
            self.current_index += 1

    def resize(self):
        currentcapacity = self.capacity
        self.capacity = self.capacity * 2
        newarray = [0] * self.capacity
        # print(self.capacity)
        for i in range(currentcapacity):
            newarray[i] = self.array[i]
        self.array = newarray

    def remove(self, item):
        if self.current_index > -1:

            for i in range(len(self.array)):
                if self.array[i] == item:
                    # print('here')
                    # print(i)
                    # print(item)
                    # #self.array[i]=0
                    # #print(self.array)
                    self.array[i] = self.array[i + 1]
                    if self.array[i] < len(self.array):
                        print(i)
                        # print(self.array[i+2])
                        self.array[i + 1] = self.array[i + 2]
                    # print(self.array[i+1])

            self.current_index -= 1
        else:
            print("Array is empty")


arr = DynamicArray()  # Creating a dynamic array

arr.add(5)  # adding elements to array
arr.add(7)
arr.add(8)
arr.add(9)
arr.add(4)
arr.remove(9)  # removing elements from array and re-ordering
arr.add(7)
print(str(arr))  # displaying array elements
print(len(arr))  # displaying array length
