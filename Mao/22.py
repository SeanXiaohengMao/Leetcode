class Solution(object):
    def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		temp = [('', 0)]
		for num in range(n*2):
			ntemp = []
			for i, t in enumerate(temp):
				st, ac = t[0], t[1]
				if ac == 0:
					ntemp.append( (st+'(' , 1 ))
				elif num+ac+1>n*2:
					ntemp.append( (st+')' , ac-1) )
				else:
					ntemp.append( (st+'(' , ac+1) )
					ntemp.append( (st+')' , ac-1) )
			temp = ntemp
		return [t[0] for t in temp]


a =  Solution().generateParenthesis(4)
b = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
print set(b)-set(a)