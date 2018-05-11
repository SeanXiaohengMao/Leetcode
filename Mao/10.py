class Solution(object):
    def isMatch(self, text, pattern):
    	memo = {}
    	def match(i ,j):
    		if (i, j) not in memo:
	    		if j == len(pattern):
	    			m = i == len(text)
	    		else:
	    			firstmatch = i<len(text) and pattern[j] in (text[i], '.')
	    			if len(pattern) > j+1 and pattern[j+1] == '*':
	    				m = match(i, j+2) or firstmatch and match(i+1, j)
	    			else:
						m = firstmatch and match(i+1, j+1)
	    		memo[i, j] = m
			return memo[i, j]
    	return match(0,0)

print Solution().isMatch("ab", ".*")