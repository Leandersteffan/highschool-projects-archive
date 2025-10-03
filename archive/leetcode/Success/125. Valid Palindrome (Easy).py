class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for i in range(len(s)):
            if 90 >= ord(s[i].upper()) >= 65 or 57 >= ord(s[i].upper()) >= 48:
                a = a + s[i].lower()
        if a == a[::-1]:
            return True
        else:
            return False
