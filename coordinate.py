def canReach(x1, y1, x2, y2,memo={}):
    if x1 == x2 and y1 == y2:
        memo[(x1,x2)] = True
        return True
    if x1 > x2 or y1 > y2:
        memo[(x1, x2)] = False
        return False
    if (x1,y1) in memo:
        return memo[(x1,y1)]
    a = canReach(x1 + y1, y1, x2, y2)
    if (x1,y1) in memo:
        return memo[(x1,y1)]
    b = canReach(x1, x1 + y1, x2, y2)
    return a or b


print(canReach(1, 1, 5, 3))
