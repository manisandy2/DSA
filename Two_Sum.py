nums = [2, 7, 11, 15]
target = 9

# Output: [0, 1]


for i in range(len(nums)):
    # print("i",i)
    for j in range(i+1,len(nums)):
        # print("j",j)
        if nums[i] + nums[j] == target:
            # print(nums[i]+nums[j])
            # print([i , j])