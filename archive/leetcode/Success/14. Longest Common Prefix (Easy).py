class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        c = strs[0]
        for i in range(len(strs)):
            prefix = ''
            if len(strs[i - 1]) < len(strs[i]):
                a = strs[i - 1]
                b = strs[i]
            else:
                b = strs[i - 1]
                a = strs[i]
            for j in range(len(a)):
                if a[j] == b[j]:
                    prefix += a[j]
                else:
                    break
            if len(prefix) < len(c):
                c = prefix 
        prefix = c
        return prefix
