class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        rows = []
        for i in range(numRows):
            rows.append([])
        order = []
        x = 0
        for i in range(len(s)):
            if x == numRows - 1:
                order.append(x)
                rows[x].append(s[i])
                x -= 1
            elif x == 0:
                order.append(x)
                rows[x].append(s[i])
                x += 1
            elif x > order[-1]:
                order.append(x)
                rows[x].append(s[i])
                x += 1
            elif x < order[-1]:
                order.append(x)
                rows[x].append(s[i])
                x -= 1
        print(rows)
        help_list = []
        for elements in rows:
            help_list += elements
        return ''.join(help_list)
