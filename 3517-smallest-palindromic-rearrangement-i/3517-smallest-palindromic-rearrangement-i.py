class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for c in s:
            freq[c] = freq.get(c,0) + 1
        m = ""
        fh = []
        for ch in sorted(freq):
            if freq[ch] % 2 == 1:
                m = ch
            fh.append(ch * (freq[ch]//2))
        fh = "".join(fh)
        return fh + m + fh[::-1]
