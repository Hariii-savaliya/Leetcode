class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = s.count('1')
        maxvalue = prev = cur = 0
        for c in s:
            if c == '0':
                cur += 1
            elif prev == 0:
                prev, cur = cur, 0
            elif prev > 0 and cur > 0:
                maxvalue = max(maxvalue, prev + cur)
                prev, cur = cur, 0 
        if prev > 0 and cur > 0:
            maxvalue = max(maxvalue, prev + cur)        
        return ones + maxvalue
        