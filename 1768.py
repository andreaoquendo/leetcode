# 1768 - Merge Strings Alternately
# Easy
# O(n)

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        new_word = ""

        if len(word1) >= len(word2):
            max_characters = len(word2)
            rest = word1[len(word2):]
        else:
            max_characters = len(word1)
            rest = word2[len(word1):]

        for i in range(max_characters):
            new_word += word1[i]
            new_word += word2[i]

        new_word += rest

        return new_word