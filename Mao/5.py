class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxl = 1
        na=nb=0
        for i in xrange(len(s)):
            a, b = self.expandlen(s, i, i)
            if b-a+1>maxl:
                maxl = b-a+1
                na, nb = a, b
            a, b = self.expandlen(s, i, i+1)
            if b-a+1>maxl:
                maxl = b-a+1
                na, nb = a, b
            # print self.expandlen(s, i, i)
            # print i, maxl
        return s[na:nb+1]
            
    def expandlen(self, s, a, b):
        lens = len(s)
        while a>=0 and b<lens:
            if s[a] != s[b]:
                break
            else:
                a-=1
                b+=1
        return a+1, b-1

print Solution().longestPalindrome("baabad")