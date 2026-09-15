class Solution:
    def climbStairs(self, n: int) -> int:
        # F(n) = F(n - 1) + F(n - 2) Fibbonacci sequence type shi desuwa
        l = [1, 1]
        for i in range(n):
            l.append(l[i] + l[i+1])
        return l[n]