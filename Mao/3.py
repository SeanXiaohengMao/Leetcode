class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) ==0:
            return 0 
        maxs = 1
        slow = 0
        quick = 0
        for quick in range(1,len(s)):
            if s[quick] in s[slow:quick]:
                maxs = max(quick-slow, maxs)
                a = s[slow:quick].index(s[quick])+1
                slow += a
        maxs = max(quick-slow+1, maxs)
        return maxs
                    