class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = big = small = nums[0]
        for i in nums[1:]:
        	big, small = max(i, i*big, i*small), min(i, i*small, i*big)
        	maxi = max(big, maxi)
        return maxi