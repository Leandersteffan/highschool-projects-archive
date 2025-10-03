class Solution:
    def fib(self, n: int) -> int:
        fib_sequence = [0, 1, 1]
        for i in range(n - 2):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]
