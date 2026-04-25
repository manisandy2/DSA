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


# Complete Python Built-in Functions
# 🔹 1. Math / Numeric
# abs(), divmod(), pow(), round()
# 🔹 2. Iterable / Sequence
# len(), max(), min(), sum()
# sorted(), reversed()
# enumerate(), zip()
# all(), any()
# 🔹 3. Functional Programming
# map(), filter()
# 🔹 4. Type Conversion
# int(), float(), complex()
# str(), bool()
# list(), tuple(), set(), dict()
# bytes(), bytearray(), memoryview()
# 🔹 5. Object & Type Inspection
# type(), isinstance(), id()
# dir(), help()
# 🔹 6. Attribute Handling (VERY IMPORTANT in frameworks)
# getattr(), setattr(), hasattr(), delattr()
# 🔹 7. Iteration Internals
# iter(), next()
# 🔹 8. String / Representation
# repr(), format(), ascii(), chr(), ord()
# 🔹 9. Input / Output
# print(), input(), open()
# 🔹 10. Execution / Dynamic Code (⚠️ Advanced)
# eval(), exec(), compile()
# 🔹 11. Scope & Variables
# globals(), locals(), vars()
# 🔹 12. Class & OOP Helpers
# super(), object()
# classmethod(), staticmethod(), property()
# 🔹 13. Import System
# __import__()
# 🔹 14. Slice & Range
# range(), slice()
# 🔹 15. Boolean & Comparison
# bool()
# 🔹 16. Hashing
# hash()
# 🔹 17. Miscellaneous
# callable(), breakpoint()