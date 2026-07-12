class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        n = int(''.join(map(str,b)))
        return (a**n)%1337
       