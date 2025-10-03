class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        x = 0
        for i in range(1, len(nums)):
            x += i
            if nums[x - 1] == nums[x]:
                nums.remove(nums[x])
                x -= 1
            x -= i
        a = 1
        b = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                a += 1
            else:
                a = 1
            if a > b:
                b = a
        return b
