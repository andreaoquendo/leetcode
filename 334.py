class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        
        right_min = nums.copy()
        left_max = nums.copy()

        i = 1
        j = len(nums) - 2
        while i < len(nums) and j >= 0:
            if right_min[i-1] > nums[i]:
                right_min[i] = nums[i]
            else:
                right_min[i] = right_min[i-1]
            
            if left_max[j+1] < nums[j]:
                left_max[j] = nums[j]
            else:
                left_max[j] = left_max[j+1]
            i+=1
            j-=1

        # for i in range(1, len(nums)):
        #     if right_min[i-1] > nums[i]:
        #         right_min[i] = nums[i]
        #     else:
        #         right_min[i] = right_min[i-1]
        
        
        # for i in range(len(nums) - 2, -1, -1):
        #     if left_max[i+1] < nums[i]:
        #         left_max[i] = nums[i]
        #     else:
        #         left_max[i] = left_max[i+1]
            
        for i, val in enumerate(nums):
            if val > right_min[i] and val < left_max[i]:
                return True
            
        return False

s = Solution()
print(s.increasingTriplet([2,1,5,0,4,6]))
