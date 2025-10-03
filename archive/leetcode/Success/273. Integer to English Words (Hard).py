class Solution:
    def numberToWords(self, num: int) -> str:
        lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        thousands = ["","Thousand","Million","Billion"]
        num = str(num)
        num_list = []
        if len(num) == 1:
            if int(num) == 0:
                return 'Zero'
            return lessThan20[int(num)]
        was_three = False
        for i in range(1, len(num)):
            i = i + 1
            if i % 3 == 0:
                num_list.append(num[-i] + num[-i+1] + num[-i+2])
                num_list.insert(0, num_list.pop(-1))
                x = i
                was_three = True
            if i == len(num) and i % 3 != 0:
                if was_three:
                    div = i - x
                else:
                    div = i
                if div == 1:
                    num_list.append(num[-i])
                elif div == 2:
                    num_list.append(num[-i] + num[-i + 1])
                num_list.insert(0, num_list.pop(-1))
        names_list = [''] * len(num_list)
        for i in range(len(num_list)):
            if len(num_list[i]) == 3 and int(num_list[i][0]) != 0 and int(num_list[i][-2:]) != 0:
                names_list[i] = names_list[i] + '' + lessThan20[int(num_list[i][0])] + ' ' + 'Hundred' + ' '
            if len(num_list[i]) == 3 and int(num_list[i][0]) != 0 and int(num_list[i][-2:]) == 0:
                names_list[i] = names_list[i] + '' + lessThan20[int(num_list[i][0])] + ' ' + 'Hundred'
            if len(num_list[i]) >= 2 and int(num_list[i][-2:]) < 20:
                names_list[i] = names_list[i] + lessThan20[int(num_list[i][-2:])]
            elif len(num_list[i]) >= 2:
                names_list[i] = names_list[i] + tens[int(num_list[i][-2])]
                if int(num_list[i][-1]) != 0:
                    names_list[i] = names_list[i] + ' ' + lessThan20[int(num_list[i][-1])]
            elif len(num_list[i]) == 1:
                names_list[i] = names_list[i] + lessThan20[int(num_list[i][-1])]
        out = ''
        while len(names_list) > 0:
            for i in range(1, len(names_list)):
                if names_list[i] != '':
                    break
                if i == len(names_list) - 1:
                    out = out + names_list[0] + f' {thousands[len(names_list) - 1]}'
                    return out
            if names_list[0] != '':
                if len(names_list) > 1:
                    out = out +  names_list[0] + f' {thousands[len(names_list) - 1]} '
                else:
                    out = out + names_list[0]
            names_list.pop(0)
        return out
