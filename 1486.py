class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = start
        for i in range(1, n):
            result ^= (start + 2*i)
        return result


s = Solution()
n = 5
start = 0
result = s.xorOperation(n, start)
print(result)