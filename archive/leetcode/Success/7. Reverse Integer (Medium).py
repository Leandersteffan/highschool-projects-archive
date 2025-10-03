class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        a = ''
        if x[0] == '-':
            for i in range(1, len(x)):
                if x[- i] != 0:
                    a = a + x[- i]
            a = '-' + a
        else:
            for i in range(1, len(x) + 1):
                if x[- i] != 0:
                    a = a + x[- i]
        if int(a) < -2**31 or int(a) > 2**31 - 1:
            return 0
        return int(a)
