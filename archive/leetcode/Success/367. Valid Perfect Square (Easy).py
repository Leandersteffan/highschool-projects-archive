class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        l, r = 0, num
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid < num < (mid+1)*(mid+1):
                return False
            elif mid * mid == num < (mid+1)*(mid+1):
                return True
            elif num < mid * mid:
                r = mid - 1
            else:
                l = mid + 1
