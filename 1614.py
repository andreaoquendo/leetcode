class Solution:
    def maxDepth(self, s: str) -> int:
        size = 0
        maxsize = size
        for el in s:
            if el == "(":
                size+=1
            elif el == ")":
                if size > maxsize:
                    maxsize = size
                size -= 1

        return maxsize

s = Solution()
print(s.maxDepth("(1)+((2))+(((3)))"))