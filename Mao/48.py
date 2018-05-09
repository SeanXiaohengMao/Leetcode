class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in xrange((n+1)/2):
        	for j in xrange(i, n-i-1):
        		matrix[j][n-i-1], matrix[n-1-i][n-j-1], matrix[n-j-1][i], matrix[i][j]  = matrix[i][j], matrix[j][n-i-1], matrix[n-1-i][n-j-1], matrix[n-j-1][i]
        		print matrix, j

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)
print matrix