class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        stack = set(nums) # runs in O(n)
        for n in nums: # runs n times
            if n not in stack: # runs about n times = O(n)
                stack.append(n)
            else:
                stack.remove(n)
        return stack


s = Solution()
result = s.singleNumber([2,3, 2, 1])
# 1 2 3 4
#
print(result)