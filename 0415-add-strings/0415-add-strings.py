class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = []
        c = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0 or c:
            if i >= 0:
                a1 = int(num1[i])
            else: a1 = 0
            if j >= 0:
                a2 = int(num2[j])
            else: a2 = 0
            t = a1 + a2 + c
            c = t//10
            ans.append(str(t % 10))
            i -= 1
            j -= 1
        return ''.join(ans[::-1])