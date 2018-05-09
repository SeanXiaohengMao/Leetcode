class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minp = 1000000000
        maxPro = 0
        for p in prices:
        	if p<minp:
        		minp = p
        	if p-minp>maxPro:
        		maxPro = p-minp
        return maxPro

print Solution().maxProfit([7,1,5,3,6,4])
