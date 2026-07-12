class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = len(haystack)
        b = len(needle)
        for i in range (a-b):
            j = 0
            while(j<b and haystack[i+j]==needle[j]):
                j+=1
            if(j==b): 
                return i        
        return -1