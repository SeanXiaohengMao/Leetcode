class Solution(object):
	def dfs(self, grid, i, j, n, m):
		# print i,j,m,n
		if i>=0 and i<m and j>=0 and j<n and grid[i][j]=='1':
			grid[i][j] = "0"
			area = self.dfs(grid, i-1, j, n, m)
			area = self.dfs(grid, i+1, j, n, m)
			area = self.dfs(grid, i, j-1, n, m)
			area = self.dfs(grid, i, j+1, n, m)


	def numIslands(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		if not grid:
			return 0
		m = len(grid)
		n = len(grid[0])
		num = 0
		for i in xrange(m):
			for j in xrange(n):
				if grid[i][j] == "1":
					self.dfs(grid, i, j, n, m)
					num+=1
		return num

print Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
