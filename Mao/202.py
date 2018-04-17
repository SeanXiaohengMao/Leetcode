class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = n
        loopli = []
        while a!=1:
        	a = self.getnum(a)
        	if a in loopli:
        		return False
        	else:
        		loopli.append(a)
        return True

    def getnum(self, n):
    	a = 0
        for i in list(str(n)):
        	i = int(i)
        	a += i*i
        return a


print Solution().isHappy(82)