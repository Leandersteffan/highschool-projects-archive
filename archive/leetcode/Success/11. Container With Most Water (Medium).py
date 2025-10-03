class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, w, area = 0, len(height) - 1, 0, 0
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            if h * w > area:
                area = h * w
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return area
