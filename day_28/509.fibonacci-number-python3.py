# @leet start
class Solution:
    def __init__(self):
        self.A = [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
            1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
            196418, 317811, 514229, 832040
        ]

    def fib(self, n: int) -> int:
        return self.A[n]
        # a,b = 1,0
        # for _ in range(n): a,b = b,a+b
        # return b

# @leet end
