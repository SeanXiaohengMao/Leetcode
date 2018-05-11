class Solution(object):
    def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		s = '1'
		for _ in range(n-1):
			sn = ''
			count = 1
			for i in range(len(s)-1):
				if s[i]==s[i+1]:
					count += 1
				else:
					sn += str(count)+s[i]
					count = 1
			sn += str(count)+s[-1]
			s = sn
		return s

print Solution().countAndSay(5)