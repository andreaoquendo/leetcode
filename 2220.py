class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start ^ goal
        return res.bit_count()

s = Solution()
print(s.minBitFlips(10, 7))