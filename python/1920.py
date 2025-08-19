class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        size = len(nums)
        ans = [0]*size
        for i in range(size):
            ans[i] = nums[nums[i]] 
        return ans

s = Solution()
print(s.buildArray([0,2,1,5,3,4]))