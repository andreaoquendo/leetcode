class Solution:
    def countBits(self, n: int) -> list[int]:
        bits = 0
        num = n
        while n != 0:
            bits+=1
            n >>= 1

        base = [0, 1]
        aux = base
        for _ in range(bits):
            aux = []
            for j in base:
                aux.append(j+1)
            base+=aux
        
        return base[:num+1]


s = Solution()
result = s.countBits(16)

# Better solution would be
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         res = [0] * (n + 1)
#         for i in range(n + 1):
#             if i % 2 == 0:
#                 res[i] = res[i // 2]
#             else:
#                 res[i] = res[i - 1] + 1
#         return res
            