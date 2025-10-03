"""def containsDuplicate(nums) -> bool:
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False"""

def containsDuplicate(nums) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


print(containsDuplicate([1,2,3,1]))