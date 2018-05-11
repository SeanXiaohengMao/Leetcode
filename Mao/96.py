# l[n] = l[0]*l[n-1]+l[1]*l[n-2]+...+l[n-1]*l[0]

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis_num = [1]
        for i in range(1,n+1):
        	num = 0
        	for m in range(i):
        		num += lis_num[0+m]*lis_num[i-1-m]
        		# print num
        	lis_num.append(num)
        	# print lis_num
        return lis_num[n]
        	
print Solution().numTrees(1)