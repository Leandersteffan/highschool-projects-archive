class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = -1
        x = 0
        for i in range(len(nums)):
            a += 1
            if nums[a - 1] == nums[a] and not a == 0:
                nums.remove(nums[a])
                a -= 1
        for i in range(len(nums)):
            b = nums[i]
            x += len(str(b))
        return x
