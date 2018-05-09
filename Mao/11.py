class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        slow = [0, height[0]]
        fast = [len(height)-1, height[-1]]
        maxa = 0
        while slow[0]<fast[0]:
        	if slow[1]<fast[1]:
        		maxa = max( maxa, (fast[0]-slow[0])*slow[1] )
        		# print maxa, fast, slow
        		slow[0]+=1
        		slow[1] = height[slow[0]]
        	else:
        		maxa = max( maxa, (fast[0]-slow[0])*fast[1] )
        		# print maxa, fast, slow
        		fast[0] -= 1
        		fast[1] = height[fast[0]]
        return maxa

