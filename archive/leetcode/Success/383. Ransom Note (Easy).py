class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        while len(ransomNote) > 0:
            index = magazine.find(ransomNote[0])
            if index == -1:
                return False
            if index == len(magazine) - 1:
                magazine = magazine[:index]
            else:
                magazine = magazine[:index] + magazine[index + 1:]
            ransomNote = ransomNote[1:]
        return True
