class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        a = m+n-1
        while m>0 and n>0:
        	if nums1[m-1]>nums2[n-1]:
        		nums1[a] = nums1[m-1]
        		m-=1
        		a-=1
        	else:
        		nums1[a] = nums2[n-1]
        		n-=1
        		a-=1
        if n>0:
            nums1[:n] = nums2[:n]
        return nums1

print Solution().merge([1,2,7,0,0,0], 3, [3,5,6], 3)