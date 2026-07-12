class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = s.lstrip()
        result = []
        b=0
        if len(a) == 0: return 0
        if(a[0] in '+-'):
             b=1
        for i in range(b,len(a)):
            if not a[i].isdigit():
                break
            else:
                result.append(a[i])
        if not result:
            return 0
        num = int(''.join(map(str, result)))
        if b==1: num = -num
        return num
       

        