class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        mod = 1337
        x=0
        for l in b:
            x+=l
            x*=10
        return pow(a,x//10,mod)
       