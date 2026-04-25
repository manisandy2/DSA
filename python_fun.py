# python build function

# len
arrow = [1,2,4,5,3,1]

print("len:",len(arrow))
# sum

print("sum:",sum(arrow))

# max 
print("max:",max(arrow))

# min
print("min:",min(arrow))

# sorted
print("sorted:",sorted(arrow))

# set
print("set:",set(arrow))

# enumerate
print("enumerate:",list(enumerate(["a","b"])))

# zip
print("Zip:",list(zip(["C","D"],["a","b"])))
print(list(zip([1,2],["a","b"])))

# map
print("map:",list(map(int,arrow)))

# filter
print("filter:",list(filter(lambda x:x ==2,arrow)))

# any
print("any:",any([True,False,True]))

# all
print("all",all([True,False,True]))
print("all",all([True,True,True]))

# range
print("Range:",list(range(1,10)))

# abs
print("abs:",abs(-7))

# Round
print("round:",round(3.752698,5))

# type
print("Type:",type(arrow))

# isinstance
print("isinstance",isinstance(123,int))
print("isinstance",isinstance("HI",str))