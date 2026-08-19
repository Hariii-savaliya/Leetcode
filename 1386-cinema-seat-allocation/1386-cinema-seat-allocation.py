class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        s = collections.defaultdict(set)
        for i,j in reservedSeats:
            if j in[2,3,4,5]:
                s[i].add(0)
            if j in[4,5,6,7]:
                s[i].add(1)
            if j in[6,7,8,9]:
                s[i].add(2)
        ans = 2*n
        for i in s:
            if len(s[i]) == 3:
                ans -= 2
            else:
                ans -= 1
        return ans