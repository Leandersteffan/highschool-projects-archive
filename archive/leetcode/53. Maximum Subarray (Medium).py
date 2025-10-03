





#Time Limit Exceeded
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        b = nums[0]
        for i in range(len(nums)):
            a = nums[i]
            x = i + 1
            for j in range(len(nums) - i - 1):
                a = a + nums[x]
                x = x + 1
                if a > b:
                    b = a
        for element in nums:
            if element > b:
                b = element
        return b
