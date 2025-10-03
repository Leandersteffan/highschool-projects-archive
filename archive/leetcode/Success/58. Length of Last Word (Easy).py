class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = -1
        x = 0
        b = string.ascii_uppercase + string.ascii_lowercase
        if len(s) > 1:
            for i in range(len(s)):
                if s[a].isalpha():
                    x += 1
                if not s[a].isalpha():
                    if not x == 0:
                        return x
                a -= 1
            return x
        else:
            if s[0].isalpha:
                return 1
