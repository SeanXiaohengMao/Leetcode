class Solution(object):
	def dfs(self, grid, i, j, area, n, m):
		# print i,j,m,n
		if i>=0 and i<m and j>=0 and j<n and grid[i][j]==1:
			grid[i][j] = 0
			area+=1
			area = self.dfs(grid, i-1, j, area, n, m)
			area = self.dfs(grid, i+1, j, area, n, m)
			area = self.dfs(grid, i, j-1, area, n, m)
			area = self.dfs(grid, i, j+1, area, n, m)
		return area 


	def maxAreaOfIsland(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		m = len(grid)
		n = len(grid[0])
		maxa = 0
		for i in xrange(m):
			for j in xrange(n):
				if grid[i][j] == 1:
					area = self.dfs(grid, i, j, 0, n, m)
					maxa = max(maxa, area)
		return maxa

print Solution().maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
