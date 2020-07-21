# Enter a list of numbers and a sum and find the number of pairs whose sum is the user inputted sum value
# use of list comprehension
list_of_numbers = [int(item) for item in input("Enter the list items : ").split()]
sum_needed = int(input("Enter the sum needed"))
ar = [(list_of_numbers[i], list_of_numbers[j])
      for i in range(len(list_of_numbers))
      for j in range(len(list_of_numbers)) if (list_of_numbers[i]+list_of_numbers[j] == sum_needed and i != j)]
print(len(ar)//2)

# can also use dict for this
# # {1: 1, 2: 2, 3: 3, 4: 4}
# m = {}
# for i in list_of_numbers:
#     m[i] = i
#
# count = 0
# for i in list_of_numbers:
#     if sum_needed - i in m:
#         count += 1


