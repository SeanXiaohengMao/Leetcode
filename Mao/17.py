class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        # dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        dic = ['', '' , 'abc', 'def',  'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        strs = ['']
        for d in digits:
        	news = []
        	for w in dic[int(d)]:
        		for s in strs:
        			news.append(s+w)
        	strs = news
        return strs

print Solution().letterCombinations('23')