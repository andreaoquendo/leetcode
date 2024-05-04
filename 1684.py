class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count = len(words)
        for word in words:
            for ch in word:
                if ch not in allowed:
                    count-=1
                    break
        return count

s = Solution()
print(s.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))