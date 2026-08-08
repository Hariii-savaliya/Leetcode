class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        for i in range(len(words)):
            w = words[i][::-1]
            words[i] = w
        return " ".join(words)