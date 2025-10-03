class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        else:
            for i in range(len(haystack)):
                if needle == haystack[i:len(needle)+i]:
                    return i
            return -1
