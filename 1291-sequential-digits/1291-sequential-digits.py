class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        s = "123456789"
        m = str(low)
        n = str(high)
        result = []
        for i in range(len(m),len(n)+1):
            for j in range(0,10-i):
                num = int(s[j:j+i])
                if low <= num <= high:
                    result.append(num)
        return result
