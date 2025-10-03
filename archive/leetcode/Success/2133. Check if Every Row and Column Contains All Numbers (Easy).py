class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        if n == 1:
            return True
        helper = []
        for i in range(1, n + 1):
            helper.append(i)
        for i in range(len(matrix)):
            if not self.check(matrix[1], helper, n):
                return False
        for col in zip(*matrix):
            if not self.check(col, helper, n):
                return False
        return True
        
    def check(self, row, helper, n):
        helper = []
        for i in range(1, n + 1):
            helper.append(i)
        for i in row:
            try:
                x = helper.index(i)
                helper[x] = 0
            except ValueError:
                return False
        return helper == [0] * len(helper)
