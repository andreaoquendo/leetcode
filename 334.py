class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:

        right_min = nums.copy()
        left_max = nums.copy()
        size = len(nums)
        i = 1
        j = size - 2
        while i < size and j >= 0:
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
            
        for i in range(size):
            if nums[i] > right_min[i] and nums[i] < left_max[i]:
                return True
            
        return False

s = Solution()
print(s.increasingTriplet([2,1,5,0,4,6]))
