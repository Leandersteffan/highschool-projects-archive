class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h = horizontalCuts[0]
        max_w = verticalCuts[0]
        for i in range(1, len(horizontalCuts)):
            if horizontalCuts[i] - horizontalCuts[i - 1] > max_h:
                max_h = horizontalCuts[i] - horizontalCuts[i - 1]
        if h - horizontalCuts[-1] > max_h:
            max_h = h - horizontalCuts[-1]

        for i in range(1, len(verticalCuts)):
            if verticalCuts[i] - verticalCuts[i - 1] > max_w:
                max_w = verticalCuts[i] - verticalCuts[i - 1]
        if w - verticalCuts[-1] > max_w:
            max_w = w - verticalCuts[-1]

        return (max_w * max_h) % ((10 ** 9) + 7)
