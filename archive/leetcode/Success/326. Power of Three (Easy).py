class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(20):
            if 3**i == n:
                return True
        return False

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            while (n % 3 == 0):
                print(n)
                n /= 3
            return n == 1
