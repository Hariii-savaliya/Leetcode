class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = ""
        c = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or c:
            if i >= 0:
                c += int(a[i])
                i -= 1
            if j >= 0:
                c += int(b[j])
                j -= 1
            s = str(c % 2) + s
            c //= 2
        return s