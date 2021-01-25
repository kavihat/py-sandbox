from string import ascii_lowercase

n = 5
k = 6
arr = [1, 5, 3, 3, 3]
dct = {}
output = []

for i in arr:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

for i in range(1, len(arr)):
    dct[arr[i]] -= 1
    if k - arr[i] in dct:
        val = [[k - arr[i], arr[i]]] * (dct[k - arr[i]])
        output.extend(val)


LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}
print(len(output))
print(LETTERS)
