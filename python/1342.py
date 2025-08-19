class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        steps = 0
        while num != 0:
            steps += 1
            if num & 1:
                steps += 1
            num >>= 1
        
        steps -= 1
            
        return steps
    
s = Solution()
result = s.numberOfSteps(8)
print(result)