class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        a = s.lstrip()
        result = []
        sign = 1
        if a[0] == '-':
            sign = -1
        elif a[0] == '+':
            sign = 1
        i = 1 if a[0] in '+-' else 0 
        for i in range(i,len(a)):
            if not a[i].isdigit():
                break
            else:
                result.append(a[i])
        if not result:
            return 0
        num = int(''.join(map(str, result)))
        if sign == -1: num = -num
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
       

        