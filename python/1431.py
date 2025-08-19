class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        result = []

        for candies_count in candies:
            result.append(candies_count + extraCandies >= max_candies)
            
        return result
      

solution = Solution()
print(solution.kidsWithCandies([1,4,5,3,2], 3))