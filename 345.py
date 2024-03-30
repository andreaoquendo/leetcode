class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        vowels = "aeiouAEIOU"
        s = list(s)
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                aux = s[i]
                s[i] = s[j]
                s[j] = aux
                i+= 1
                j-=1 
            if s[i] not in vowels:
                i+= 1
            if s[j] not in vowels:
                j-=1

        return "".join(s)

s = Solution()
print(s.reverseVowels("abe"))