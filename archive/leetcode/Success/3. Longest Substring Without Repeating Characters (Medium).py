class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        b = 1
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            x = 1
            check = []
            for j in range(i + 1, len(s)):
                if s[i] != s[j] and not check.count(s[j]):
                    x += 1
                    check.append(s[j])
                    if x > b:
                        b = x
                else:
                    break
        return b
