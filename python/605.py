class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        ones = 0
        zeros = 0
        isFirst = True
        for flower in flowerbed:
            if flower == 1:
                ones += 1
                if isFirst:
                    if zeros%2 == 0:
                        zeros+=1
                    isFirst = False

                if zeros == 0:
                    continue
                quantity = (zeros - 1)// 2
                zeros = 0
                n -= quantity
                if n <= 0:
                    return True
            else:
                zeros+=1
        
        if zeros > 0 and ones > 0:
            if zeros%2 == 0:
                zeros+=1
            quantity = (zeros - 1)// 2
            zeros = 0
            n -= quantity
            if n <= 0:
                return True
        elif zeros > 0 and ones == 0:
            if zeros % 2 == 1:
                max_quantity = zeros // 2 + 1
                if n <= max_quantity:
                    return True
            else:
                max_quantity = zeros // 2
                if n <= max_quantity:
                    return True
        
        return False


solution = Solution()
print(solution.canPlaceFlowers([0,0, 0],2))
    