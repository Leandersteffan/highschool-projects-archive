class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = ''.join(map(str, digits))
        x = int(x)
        x += 1
        return list(map(int, str(x)))
        
        '''digits[-1] += 1
        digits.reverse()
        for i in range(len(digits)):
            if i == len(digits) - 1 and digits[i] > 9:
                digits[i] -= 10
                digits.insert(len(digits), 1)
            if digits[i] > 9:
                digits[i] -= 10
                digits[i + 1] += 1
        digits.reverse()
        return digits'''
