class Solution(object):
    def twoSum(self, nums, s):
    	lis = []
    	dic = {}
    	for num in nums:
    		# print nums
    		# print num, dic[num]
    		# print dic
    		if num in dic:
    			# print num, dic[num]
    			# print lis
    			if dic[num]!=None:
	    			lis.append([num, dic[num]])
	    			dic[num] = None
    				dic[s - num] = None
    		else:
    			dic[s - num] = num	
    	return lis			

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rl = []
        nums.sort()
        prev = 1
        for i, num in enumerate(nums):
        	if num>0:
        		break
        	if num!=prev:
        		# print "adasdasd"
	        	lis = self.twoSum(nums[i+1:], -num)
	        	# print lis
	        	for l in lis:
	        		l.append(num)
	        		rl.append(l)
	        # print rl
	        prev = num
        return rl

print Solution().threeSum([0,2,2,3,0,1,2,3,-1,-4,2])