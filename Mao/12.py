class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        w = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        st = ''
        for i, v in enumerate(val):
        	while num - v >=0:
        		num -= v
        		st += w[i]
        	if num == 0:
        		break
        return st

print Solution().intToRoman(20)