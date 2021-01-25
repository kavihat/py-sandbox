def are_they_equal(array_a, array_b):
    array_a.sort()
    array_b.sort()
    print("array a",array_a)
    print("array b",array_b)
    if array_a==array_b:
        return True
    else:
        return False

print(are_they_equal([1,2,3,4],[1,2,3,3]))