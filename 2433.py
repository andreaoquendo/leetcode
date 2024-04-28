class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        if not pref:
            return []
        
        size = len(pref)
        res = [0]*size
        res[0] = pref[0]

        for i in range(1, size):
            res[i] = pref[i-1] ^ pref[i]

        return res
    
s = Solution()
print(s.findArray([5,2,0,3,1]))