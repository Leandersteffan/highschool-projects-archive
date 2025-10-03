class Solution:
    def climbStairs(self, n: int) -> int:
        liste = [1,2]
        for i in range(n - 2):
            liste.append(liste[-1] + liste[-2])
        return liste[n - 1]
