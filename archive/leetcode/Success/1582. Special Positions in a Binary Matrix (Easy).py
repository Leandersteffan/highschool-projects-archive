class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        x = 0
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    i_is = True
                    j_is = True
                    for c in range(m):
                        if c != i and mat[c][j] == 1:
                            i_is = False
                    if i_is:
                        for v in range(n):
                            if v != j and mat[i][v] == 1:
                                j_is = False
                    if i_is and j_is:
                        x += 1
        return x
