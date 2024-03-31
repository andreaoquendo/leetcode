class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        max_flag = False
        min_flag = False

        size = len(nums)
        min_arr = [False]*size
        max_arr = [False]*size
        final_arr = [False]*size

        # ida
        for i, n in enumerate(nums):
            if min_flag:
                if n < minK:
                    min_flag = False
                else:
                    min_arr[i] = True
            
            if n == minK:
                min_arr[i] = True
                min_flag = True
            
            if max_flag:
                if n > maxK:
                    max_flag = False
                else:
                    max_arr[i] = True
            
            if n == maxK:
                max_arr[i] = True
                max_flag = True
        
        # volta
        for i in range(size - 1, -1, -1):
            if min_flag:
                if nums[i] < minK:
                    min_flag = False
                else:
                    min_arr[i] = True
            
            if nums[i] == minK:
                min_arr[i] = True
                min_flag = True
            
            if max_flag:
                if nums[i] > maxK:
                    max_flag = False
                else:
                    max_arr[i] = True
            
            if nums[i] == maxK:
                max_arr[i] = True
                max_flag = True

        for i in range(size):
            final_arr[i] = min_arr[i] and max_arr[i]
        
        print(min_arr)
        print(max_arr)
        print(final_arr)



s = Solution()
print(s.countSubarrays([1,3,5,2,7,5], 1, 5))