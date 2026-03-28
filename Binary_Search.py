arroy = [0,1,2,6,8,7,9,12,52]
traget = 5

arrow_sorted = sorted(arroy)
    
left = 0
right = len(arrow_sorted)-1


while left <= right:
    print("left:",left)
    print("right:",right)
    mid = (left+right)//2
    print("mid",mid)
    print("#"*12)
    if traget == arrow_sorted[mid]:
        print("traget value found:",mid)
        print("value:",arrow_sorted[mid])
        break
    elif traget > arrow_sorted[mid]:
        left = mid+1
    elif traget < arrow_sorted[mid]:
        right = mid-1
