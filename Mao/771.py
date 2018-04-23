class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        a = set(J)
        num = 0
        for i in S:
        	if i in a:
        		num += 1
        print num