class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for _ in xrange(len(nums)):
        	if not nums[i]:
        		del(nums[i])
        		nums.append(0)
        	else:
        		i+=1
        	# print i, nums


