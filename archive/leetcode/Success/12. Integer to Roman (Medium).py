class Solution:
    def intToRoman(self, num: int) -> str:
        values = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for x in values:
            while x <= num:
                res += values[x]
                num -= x
        return res
    
'simular as good but more data usage'
class Solution:
    def intToRoman(self, num: int) -> str:
        values = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        values_revers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        max_possible = [1000, 500, 100, 50, 10, 5, 1]
        max_possible_revers = sorted(max_possible)
        roman_unfin = []
        for i in range(len(max_possible)):
            if max_possible[i] == 1000 or max_possible[i] == 100 or max_possible[i] == 10 or max_possible[i] == 1:
                one_front = True
            if max_possible[i] == 500 or max_possible[i] == 50 or max_possible[i] == 5:
                one_front = False
            pos = max_possible_revers.index(max_possible[i])
            while num - max_possible[i] >= 0:
                num -= max_possible[i]
                roman_unfin.append(max_possible[i])
            clip = str(num)
            if one_front and int(clip[0]) != 9:
                pass
            else:
                for j in range(pos - 1, pos + 1):
                    "print(i, j, pos, num, f'/ {num} - {max_possible[i]} + {max_possible[-j]}')"
                    if j > 0 and max_possible[-j] == 1 or max_possible[-j] == 10 or max_possible[-j] == 100:
                        if num - max_possible[i] + max_possible[-j] >= 0:
                            num = (num - max_possible[i]) + max_possible[-j]
                            roman_unfin.append(max_possible[-j])
                            roman_unfin.append(max_possible[i])
        roman = ''
        for i in range(len(roman_unfin)):
            if roman_unfin[i] != 0:
                roman = roman + values[roman_unfin[i]]
        return roman
