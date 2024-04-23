class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:

        result = []
        result.append(first)
        i = 0
        for item in encoded:
            result.append(item ^ result[i])
            i+=1
        return result
    

s = Solution()
print(s.decode([6,2,7,3], 4))
    

