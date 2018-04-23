class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num = 0
        n = len(grid)
        m = len(grid[0])
        for i in xrange(n):
        	for j in xrange(m):
        		if grid[i][j] == 1:
        			num += 4
        			if j>=1 and grid[i][j-1] == 1:
        				num -= 1
        			if j+1<=m-1 and grid[i][j+1] == 1:
        				num -= 1
        			if i>=1 and grid[i-1][j] == 1:
        				num -= 1
        			if i+1<=n-1 and grid[i+1][j] == 1:
        				num -= 1
        return num