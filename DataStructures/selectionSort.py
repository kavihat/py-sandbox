ar = [5, 2, 3, 1]
for i in range(len(ar)):
    minimum = i
    for j in range(i + 1, len(ar)):
        if ar[j] < ar[minimum]:
            minimum = j
    ar[i],ar[minimum]= ar[minimum],ar[i]
print(ar)
