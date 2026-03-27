arr = [2, 4, 6, 8, 10]

prefix = [2, 6, 12, 20, 30]

# prefix[i] = prefix[i-1] + arr[i]

def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    
    prefix[0] = arr[0]
    
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
        print(prefix[i-1])
    
    return prefix


def range_sum(prefix, L, R):
    if L == 0:
        return prefix[R]
    return prefix[R] - prefix[L-1]


# Example
arr = [2, 4, 6, 8, 10]
prefix = [2, 6, 12, 20, 30]
