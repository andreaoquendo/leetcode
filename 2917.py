class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        total = 0
        for i in range(32):
            bit = 1<<i
            q = 0
            for n in nums:
                if n & bit:
                    q+=1
            if q >= k:
                total += bit
        

        return total




s = Solution()
result = s.findKOr([6], 3)
print(result)