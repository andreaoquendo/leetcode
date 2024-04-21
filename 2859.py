class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        total = 0

        for index, n in enumerate(nums):
            sum = 0
            number = index
            while number > 0:
                if number%2 == 1:
                    sum+=1
                number = number // 2
            
        return total
    

s = Solution()
result = s.sumIndicesWithKSetBits([5,10,1,5,2], 1)
print(result)
