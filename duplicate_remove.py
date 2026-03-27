
# Burte force
def findDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1 ,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
    

def findDuplicate02(nums):
    seen = set()
    for num in nums:
        
        if num in seen:
            return True
        seen.add(num)
        print(seen)
    return False


def findDupicate03(nums):
    return len(nums) != len(set(nums))

if __name__== "__main__":
    nums= [1,2,3,1]
    # nums= [1,2,3,4]
    print(findDupicate03(nums))

