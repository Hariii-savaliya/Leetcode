class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        c = 0
        i = j = 0
        g.sort()
        s.sort()
        
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                c += 1
                i += 1
                
            j+=1
        return c    