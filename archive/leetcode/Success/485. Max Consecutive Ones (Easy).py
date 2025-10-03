class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        output = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                x += 1
            else:
                output = max(x, output)
                x = 0
        return max(x, output)
