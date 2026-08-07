class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        for i in range(len(words)):
            words[i] = words[i].lower()
            if len(words[i]) > 2:
                words[i] = words[i].title()
        ans = " ".join(words)
        return ans