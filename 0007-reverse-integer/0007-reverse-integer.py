class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        mx = 2**31 - 1
        mn = -2**31
        sign = 1
        if x<0: sign = -1
        x = abs(x)
        while x!=0:
            c = x%10
            
            rev = rev*10 + c
            x = int(x//10)
        rev *=sign
        if(rev>mx or rev<mn):
                return 0

        return rev
        
       

        
        