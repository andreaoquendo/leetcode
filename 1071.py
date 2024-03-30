class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        length = min(len(str1), len(str2))

        if str1[:length] != str2[:length]:
            return ""
        
        
        keyword = str1[:length]
        great_word = ""

        if str1 == str2:
            return keyword
        elif len(str1) > len(str2):
            great_word = str1
        else:
            great_word = str2

        i = len(keyword)
        final_keyword = ""
        while i > 0:
            while len(keyword) % i != 0 or len(great_word) % i != 0:
                i -=1
            
            idx = i
            flag = False
            while idx+i <= len(keyword):
                if keyword[idx:idx+i] != keyword[:i]:
                    flag = True
                    break
                idx+=i
            
            if flag == True:
                i -= 1
                continue
            flag = False
            
            while idx+i <= len(great_word):
                if great_word[idx:idx+i] != keyword[:i]:
                    flag = True
                    break
                idx+=i

            if flag == True:
                i -= 1
                continue

            final_keyword = keyword[:i]
            break

        return final_keyword    