class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        count = 0
        for c in s[::-1]:
            if count > 0 and c == " ":
                return count
            if c != " ":
                count+=1

        return count
    
s = Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))