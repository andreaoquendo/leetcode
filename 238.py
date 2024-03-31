# def needed help

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        size = len(nums)
        prefix = [1]*size
        postfix = [1]*(size + 1)

        for i in range(size):
            prefix[i] = prefix[i-1]*nums[i]

        for i in range(size -1, -1, -1):
            postfix[i] = postfix[i+1]*nums[i]
        postfix = postfix[:-1]

        for i in range(size):
            if i - 1 < 0:
                nums[i] = 1*postfix[i+1]
            elif i + 1 >= size:
                nums[i] = 1*prefix[i-1]
            else:
                nums[i] = prefix[i-1]*postfix[i+1]

        return nums


s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))
