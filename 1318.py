class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(32):
            mask = 1<<i
            a_mask, b_mask, c_mask = a & mask, b & mask, c & mask
            if a_mask| b_mask == c_mask:
                continue
            else:
                flips+= 1
                if c_mask == 0 and a_mask & b_mask:
                    flips += 1

        return flips

s = Solution()
print(s.minFlips(1, 2, 3))