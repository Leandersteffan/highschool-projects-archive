class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
        while True:
            try:
                nums.remove('_')
            except ValueError:
                return len(nums)
