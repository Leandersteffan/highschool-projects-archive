class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_num_dir = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        inp = list(digits)
        out = []
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return digit_num_dir[digits]
        elif len(digits) == 2:
            for i in range(len(digit_num_dir[digits[0]])):
                for j in range(len(digit_num_dir[digits[1]])):
                    out.append(digit_num_dir[digits[0]][i] + digit_num_dir[digits[1]][j])
            return out
        elif len(digits) == 3:
            for i in range(len(digit_num_dir[digits[0]])):
                for j in range(len(digit_num_dir[digits[1]])):
                    for k in range(len(digit_num_dir[digits[2]])):
                        out.append(digit_num_dir[digits[0]][i] + digit_num_dir[digits[1]][j] + digit_num_dir[digits[2]][k])
            return out
        elif len(digits) == 4:
            for i in range(len(digit_num_dir[digits[0]])):
                for j in range(len(digit_num_dir[digits[1]])):
                    for k in range(len(digit_num_dir[digits[2]])):
                        for l in range(len(digit_num_dir[digits[3]])):
                            out.append(digit_num_dir[digits[0]][i] + digit_num_dir[digits[1]][j] + digit_num_dir[digits[2]][k] + digit_num_dir[digits[3]][l])
            return out
