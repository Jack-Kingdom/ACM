class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(' ')
        s=[word[::-1] for word in s]
        s=' '.join(s)
        return s
